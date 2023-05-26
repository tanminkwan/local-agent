import os
import sys
import signal
import threading
from time import sleep
from importlib import import_module
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
#import logging
#import logging.handlers
from .app_config import AppConfig
from .executer import ExecuterCaller
from .command_reciever import CommandsReciever
from .event_reciever import Command
from .message_reciever import MessageReciever
from .flask_zipkin import Zipkin

__version__ = '0.0.8'

#Load configuration
configure = AppConfig(os.getcwd())
configure.from_pyfile('config.py')

#Set logging
"""
fileHandler = logging.handlers.TimedRotatingFileHandler(
    filename='./log.txt', 
    when = "D" ,
    backupCount= 7 , 
    atTime=None
    )

fileHandler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
                              "%Y-%m-%d %H:%M:%S")
fileHandler.setFormatter(formatter)
logging.basicConfig(handlers=[fileHandler])
"""

#Get flask handle
app_name = configure['AGENT_NAME'] \
    if configure.get('AGENT_NAME') else __name__
app = Flask(app_name)

#enable CORS for all routes 
CORS(app)

# zipkin
zipkin = None
if configure.get('ZIPKIN_ADDRESS'):
    zipkin = Zipkin(app, sample_rate=100)
    app.config['ZIPKIN_ADDRESS']=configure['ZIPKIN_ADDRESS']

#REST API
api = Api(app, prefix="/api/v1")
api.add_resource(Command, '/command')

if configure.get('CUSTOM_APIS_PATH'):
    import_module(configure['CUSTOM_APIS_PATH'])

#local database
if not configure.get('SQLALCHEMY_DATABASE_URI'):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    configure['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'app.db')

app.config ['SQLALCHEMY_DATABASE_URI'] = configure['SQLALCHEMY_DATABASE_URI']

db = SQLAlchemy(app)
#Job Scheduler
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

#Executer
executer = ExecuterCaller.instance(configure)

#Interept Event
stop_event = threading.Event()

def signal_handler(sig, frame):
    global stop_event
    stop_event.set()
    sys.stderr.write("KeyboardInterrupt received, stopping...\n")
    sleep(5)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#Command Reciever (Web url polling)
command_reciever = None
if configure.get('COMMANDER_SERVER_URL'):
    command_reciever = CommandsReciever(configure['COMMANDER_SERVER_URL'], stop_event)

#Table creation
# 1. miniagent tables
from . import models
# 2. custom tables
if configure.get('CUSTOM_MODELS_PATH'):
    mdl = import_module(configure['CUSTOM_MODELS_PATH'])
    cls_objs = [x for x in mdl.__dict__ if not x.startswith("_")]
    globals().update({k: getattr(mdl, k) for k in cls_objs})

with app.app_context():
    db.create_all()

#Kafka
message_reciever = None
if configure.get('EXECUTERS_BY_TOPIC') and configure.get('KAFKA_BOOTSTRAP_SERVERS'):
    message_reciever = MessageReciever(
        group_id = configure['AGENT_NAME'],
        executers_by_topic = configure['EXECUTERS_BY_TOPIC'],
        event = stop_event
    )

#Start scheduled jobs
if configure.get('SCHEDULED_JOBS'):
    from .job_reciever import ScheduledJob
    ScheduledJob(executer, configure['SCHEDULED_JOBS'])
