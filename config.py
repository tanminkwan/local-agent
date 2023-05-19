import os
from datetime import datetime, timedelta

AGENT_NAME = 'BLUE_SKULL_NO13'

ZIPKIN_ADDRESS = ('localhost',9411)

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "example.model"

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

EXECUTERS_BY_TOPIC =\
{
    "TEST_TOPIC":
    "example.executer.say_hello.PrintParam",
    "TEST2_TOPIC":
    "example.executer.say_hello.PrintParam",
}

DEFAULT_ADAPTEES =\
{
    "example.adapter.restserver_adapters.RESTServerAdapter":
    "example.adaptee.tadaptees.RESTServer",
    "example.adapter.printer_adapters.PrinterAdapter":
    "example.adaptee.tadaptees.CardPrinterAdaptee",
    "example.adapter.payment_adapters.PaymentAdapter":
    "example.adaptee.tadaptees.CreditCardPaymentAdaptee",
}
"""

SCHEDULED_JOBS =\
[
    {
        "executer":"example.executer.scheduler.DeviceHealth",
        "trigger":"interval",
        "id":"DeviceHealth",
        "name":"Devices Health Check",
        "minutes":20,
        "start_date":datetime.now()+timedelta(minutes=1)
    }
]

    {
        "executer":"example.executer.scheduler.DeviceHealth2Kafka",
        "trigger":"interval",
        "id":"DeviceHealth2",
        "name":"Devices Health Check2",
        "minutes":30,
        "start_date":datetime.now()+timedelta(minutes=1)
    },
"""
