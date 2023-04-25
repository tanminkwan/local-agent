import os
from datetime import datetime, timedelta

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "addin.model"

DEFAULT_ADAPTERS =\
{
    "PrinterAdapterInterface":
    "addin.adapter.printer_adapters.PrinterAdapter",
    "PaymentAdapterInterface":
    "addin.adapter.payment_adapters.PaymentAdapter",
    "RESTServerAdapterInterface":
    "addin.adapter.restserver_adapters.RESTServerAdapter",
}
DEFAULT_ADAPTEES =\
{
    "addin.adapter.restserver_adapters.RESTServerAdapter":
    "addin.adaptee.tadaptees.RESTServer",
    "addin.adapter.printer_adapters.PrinterAdapter":
    "addin.adaptee.tadaptees.CardPrinterAdaptee",
    "addin.adapter.payment_adapters.PaymentAdapter":
    "addin.adaptee.tadaptees.CreditCardPaymentAdaptee",
}
SCHEDULED_JOBS =\
[
    {
        "executer":"addin.executer.scheduler.DeviceHealth",
        "trigger":"interval",
        "id":"DeviceHealth",
        "name":"Devices Health Check",
        "minutes":5,
        "start_date":datetime.now()+timedelta(minutes=1)
    }
]