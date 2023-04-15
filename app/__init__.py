import os
from flask import Flask
from flask_restful import Api
from flask_apscheduler import APScheduler
from .app_config import AppConfig
from .executer import Executer
from .commands_reciever import CommandsReciever
from .adapters import PrinterAdapter
from .events_reciever_apis import Command

configure = AppConfig(os.getcwd())
configure.from_pyfile('config.py')

app = Flask(__name__)

api = Api(app, prefix="/api/v1")
api.add_resource(Command, '/command')

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

executer = Executer.instance()
reciever = CommandsReciever(configure['COMMANDER_SERVER_URL'], executer)