from kafka import KafkaProducer
import json
from miniagent import configure
from miniagent.adapter import Adapter
from miniagent.common import SingletonInstane


class KafkaProducerAdapter(Adapter):

    producer = None

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=configure['KAFKA_BOOTSTRAP_SERVERS'])

    def produce_message(self, topic: str, message: dict) -> tuple[int, dict]:
        self.producer.send(topic,json.dumps(message).encode('utf-8'))
        return 1, {'message':'OK'}
    
    def __del__(self):
        print('del KafkaProducerAdapter')
        if self.producer:
            self.producer.close()

    def get_status(self) -> int:
        return 1