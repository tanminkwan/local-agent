import os
from flask import Flask
from flask_restful import Api
from flask_apscheduler import APScheduler
from flask_sqlalchemy import SQLAlchemy
import logging
import logging.handlers
from datetime import datetime
from .app_config import AppConfig
from .executer import ExecuterCaller
from .commands_reciever import CommandsReciever
from .events_reciever_apis import Command

configure = AppConfig(os.getcwd())
configure.from_pyfile('config.py')

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

app = Flask(__name__)

api = Api(app, prefix="/api/v1")
api.add_resource(Command, '/command')

app.config ['SQLALCHEMY_DATABASE_URI'] = configure['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

#executer = ExecuterCaller.instance(configure)
#reciever = CommandsReciever(configure['COMMANDER_SERVER_URL'], executer)

executer = ExecuterCaller.instance(configure)
reciever = CommandsReciever(configure['COMMANDER_SERVER_URL'])

from . import models
from addin.model import *

with app.app_context():
    db.create_all()
