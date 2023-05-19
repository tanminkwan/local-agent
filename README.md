# Miniagent

Miniagent is a multi-adaptable and lightweight server framework based on **Flask**.

## Installing

Install and update using **pip**:
```
$ pip install -U miniagent
```

## Advised Virtual Environment Install

Virtual env is highly advisable because the more projects you have, the more likely it is that you will be working with different versions of Python itself, or at least different versions of Python libraries.

```
$ pip install virtualenv
```
Next create a virtualenv:
```
$ virtualenv venv
New python executable in venv/bin/python
Installing distribute............done.
$ . venv/bin/activate
(venv)$
```
Now install miniagent on the virtual env, it will install all the dependencies and these will be isolated from your system’s python packages

```
(venv)$ pip install miniagent
```

## Example code download

Create an example project after installing miniagent

`$ mini-project tanminkwan/local-agent test_project`

Then test_project directory and files are created like the tree below.
```
└── test_project
    ├── run.py
    ├── config.py
    └── myapp
        ├── __init__.py
        ├── adaptee.py
        ├── adapter.py
        ├── dbquery.py
        ├── executer.py
        └── model
            ├── __init__.py
            └── mymodels.py
```

## A Simple Example

There must be two files config.py and run.py in the base directory.
```
# this is a sample config.py
import os
from datetime import datetime, timedelta

AGENT_NAME = 'BLUE_SKULL_NO13'

ZIPKIN_ADDRESS = ('localhost',9411)

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "myapp.model"

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
    "myapp.adapter.printer_adapters.PrinterAdapter":
    "myapp.adaptee.tadaptees.CardPrinterAdaptee",
    "myapp.adapter.payment_adapters.PaymentAdapter":
    "myapp.adaptee.tadaptees.CreditCardPaymentAdaptee",
}
SCHEDULED_JOBS =\
[
    {
        "executer":"myapp.executer.scheduler.DeviceHealth",
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