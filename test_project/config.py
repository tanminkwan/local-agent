import os
from datetime import datetime, timedelta

AGENT_NAME = 'BLUE_SKULL_NO13'

COMMANDER_SERVER_URL = 'http://localhost:8809'

base_dir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')

CUSTOM_MODELS_PATH = "myapp.model"

KAFKA_BOOTSTRAP_SERVERS = ['localhost:9092']

EXECUTERS_BY_TOPIC =\
{
    "TEST_TOPIC":
    "myapp.executer.PrintParam",
}

DEFAULT_ADAPTEES =\
{
    "myapp.adapter.TestAdapterWithAdaptee":
    "myapp.adaptee.TestAdaptee",
}

SCHEDULED_JOBS =\
[
    {
        "executer":"myapp.executer.DeviceHealth",
        "trigger":"interval",
        "id":"DeviceHealth",
        "name":"Devices Health Check",
        "minutes":5,
        "start_date":datetime.now()+timedelta(minutes=1)
    }
]