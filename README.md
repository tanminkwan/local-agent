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
## Configuration Variables

Configuration variables defined in the config.py file

|Variable|Type|Description|Default|
|--|--|--|--|
|DEBUG|_bool_|Debug mode y/n|True
|AGENT_NAME|_str_|It is used to identify a specific service.|main .py file name|
|AGENT_ROLES|_list_ or _str_|REST api, message receiver, and scheduler job resources defined in miniagent can grant authority only to specific roles. This variable is useful when implementing services of multiple roles with one application. <p> **ex** : `AGENT_ROLES = "customer,tester"`|
|COMMAND_RECEIVER_ENABLED|_bool_|It indicates whether to use Command Receiver or not.|False|
|COMMANDER_SERVER_URL|_str_|URL to be polled by Command Receiver|
|COMMANDER_RESPONSE_CONVERTER|_str_| Path of function that processes the response received by Command Receiver so that Executor can process it.  If it is not defined, the response is sent to Executor without being processed. <p> **ex** : `COMMANDER_RESPONSE_CONVERTER = "example.etc.command_converter"`|
|MESSAGE_RECEIVER_ENABLED|_bool_|It indicates whether to use Message Receiver(Kafka consumer) or not.|False|
|KAFKA_BOOTSTRAP_SERVERS|_list(str)_|A list of kafka bootstrap servers to be called by Message Receiver|
|EXECUTERS_BY_TOPIC|_list(dir)_|Kafka topics to be polled by Message Receiver and Executors to handle processing for each topic. <p> **ex** : `EXECUTERS_BY_TOPIC =[{"topic":"TEST_TOPIC",    "executer":"example.executer.say_hello.PrintParam", "agent_roles":["tester","admin"]}]`|
|SQLALCHEMY_DATABASE_URI|_str_|URI of dedicated database of the service|`"sqlite:///" + os.path.join(base_dir, "app.db")`|
|CUSTOM_MODELS_PATH|_str_|Path of data models added by the application <p> **ex** : `CUSTOM_MODELS_PATH = "example.model"`
|CUSTOM_APIS_PATH|_str_|Path of REST APIs added by the application <p> **ex** : `CUSTOM_APIS_PATH = "example.api"`
|TIMEZONE|_str_|Timezone to be used in miniagent <p> **ex** : `TIMEZONE = "Asia/Seoul"`|
|SCHEDULER_API_ENABLED|_bool_|It indicates whether to open REST APIs of Job Scheduler or not.|False|
|EXIT_AFTER_JOBS|_bool_|It indicates whether to terminate the service when all jobs scheduled in Job Scheduler are finished.|False|
|SCHEDULED_JOBS|_list(dir)_|List of jobs to be scheduled in Job Scheduler|
|DEFAULT_ADAPTEES|_dir_|If the application uses a 3rd party solution, register the 3rd party solution library as an adaptee and develop an adapter so that the executor can use it. That variable defines the mapping of adapters and adaptees.|
|ZIPKIN_ADDRESS|_tuple(str,int)_|Zipkin server address. <p> **ex** : `ZIPKIN_ADDRESS = ("localhost",9411)`|

## Sample code download

Create an sample project after installing miniagent

`$ mini-project tanminkwan/banking-poc /`

Then the source files are downloaded from Github on the current directory. The following is the directory tree.
```
├── banking  
│   ├── __init__.py  
│   ├── api  
│   │   ├── __init__.py  
│   │   ├── bapis.py  
│   ├── dbquery  
│   │   └── queries.py  
│   ├── executer  
│   │   ├── __init__.py  
│   │   ├── deposit.py  
│   │   ├── event.py  
│   │   └── raffle.py  
│   └── model  
│       ├── __init__.py  
│       └── models.py  
├── app.py  
├── config.py  
├── bonnie.py  
├── clyde.py  
├── john_dillinger.py  
├── deposit.py  
├── event.py  
└── raffle.py
```
## Run Kafka, Opensearch and Zipkin services

Run Kafka, Opensearch and Zipkin and register the endpoints of them in config.py.
```
ZIPKIN_DOMAIN_NAME = 'localhost'
ZIPKIN_PORT =  '9411'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
ELASTIC_SEARCH_DOMAIN_NAME = 'localhost'
ELASTIC_SEARCH_PORT = '9200'
```
## Run the six applications

Run the five applications as below.
```
$ nohup python raffle.py &
$ nohup python deposit.py &
$ nohup python event.py &
$ nohup python clyde.py &
$ nohup python bonnie.py &
$ nohup python john_dillinger.py &
```
## Open Zipkin web site and check the transactions

1. Clyde and Bonnie send requests to Deposit and Event every 30 seconds. 
2. Deposit produces messages and Raffle consumes the messages via Kafka. 
3. Event calls Raffle whenever it receive a request from Clyde and Bonnie. 
4. John Dillinger requests deposit amount by account from Event every 30 seconds. 
5. Event retrieves this information from Opensearch and provides it to John Dillinger. 

You can see all of them on the Zipkin dashboard.(Maybe http://localhost:9411)
