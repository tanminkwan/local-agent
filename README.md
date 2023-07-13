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

1. Clyde and Bonnie send requests to Deposit and Event every 2 minites. 
2. Deposit produces messages and Raffle consumes the messages via Kafka. 
3. Event calls Raffle whenever it receive a request from Clyde and Bonnie. 
4. John Dillinger requests deposit amount by account from Event every 4 minutes. 
5. Event retrieves this information from Opensearch and provides it to John Dillinger. 

You can see all of them on the Zipkin dashboard.(Maybe http://localhost:9411)
