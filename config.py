import os
from datetime import datetime, timedelta

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "example.model"

DEFAULT_ADAPTEES =\
{
    "example.adapter.restserver_adapters.RESTServerAdapter":
    "example.adaptee.tadaptees.RESTServer",
    "example.adapter.printer_adapters.PrinterAdapter":
    "example.adaptee.tadaptees.CardPrinterAdaptee",
    "example.adapter.payment_adapters.PaymentAdapter":
    "example.adaptee.tadaptees.CreditCardPaymentAdaptee",
}
SCHEDULED_JOBS =\
[
    {
        "executer":"example.executer.scheduler.DeviceHealth",
        "trigger":"interval",
        "id":"DeviceHealth",
        "name":"Devices Health Check",
        "minutes":5,
        "start_date":datetime.now()+timedelta(minutes=1)
    }
]