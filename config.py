import os
from datetime import datetime, timedelta

AGENT_NAME = 'BLUE_SKULL_NO13'

ZIPKIN_ADDRESS = ('localhost',9411)

COMMANDER_SERVER_URL = 'http://localhost:8809'
COMMANDER_RESPONSE_CONVERTER = "example.etc.command_converter"

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "example.model"

CUSTOM_APIS_PATH = "example.api"

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

AGENT_ROLES = "customer,tester"

EXECUTERS_BY_TOPIC =\
[
    {"topic":"TEST_TOPIC",
    "executer":"example.executer.say_hello.PrintParam",
     "agent_roles":["tester","admin"]},
]

DEFAULT_ADAPTEES =\
{
    "example.adapter.restserver_adapters.RESTServerAdapter":
    "example.adaptee.tadaptees.RESTServer",
    "example.adapter.printer_adapters.PrinterAdapter":
    "example.adaptee.tadaptees.CardPrinterAdaptee",
    "example.adapter.payment_adapters.PaymentAdapter":
    "example.adaptee.tadaptees.CreditCardPaymentAdaptee",
}

EXIT_AFTER_JOBS = False
SCHEDULED_JOBS =\
[
    {
        "executer":"example.executer.scheduler.DeviceHealth",
        "trigger":"interval",
        "id":"DeviceHealth",
        "name":"Devices Health Check",
        "minutes":2,
        "start_date":datetime.now()+timedelta(minutes=1),
        "agent_roles":["tester","admin"]
    },
]
"""
    {
        "executer":"example.executer.scheduler.DeviceHealth2Kafka",
        "trigger":"interval",
        "id":"DeviceHealth2",
        "name":"Devices Health Check2",
        "minutes":2,
        "start_date":datetime.now()+timedelta(minutes=1)
    },
"""
