# Miniagent

Miniagent is a multi-adaptable and lightweight application framework based on **Flask**.

## Installing

Install and update using **pip**:
`$ pip install -U miniagent`

## A Simple Example

There must be two files config.py and run.py in the base directory.
```
# this is a sample config.py
import os
from datetime import datetime, timedelta

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "example.model"

DEFAULT_ADAPTEES =\
{
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
```
```
# save this as run.py
from miniagent import app

app.run(host="0.0.0.0", port=17080, use_reloader=False, debug=True)
```
```
$ python run.py
  * Running on http://127.0.0.1:17080/ (Press CTRL+C to quit)
```