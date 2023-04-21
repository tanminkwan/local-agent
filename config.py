import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
COMMANDER_SERVER_URL = 'http://localhost:8809'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

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
    "addin.adapter.db_adapters.Purchase":
    "addin.adaptee.tadaptees.Sqlite3Adaptee",
}
SCHEDULED_JOBS =\
{
    
}