from kafka import KafkaProducer
import json
from miniagent import configure
from miniagent.adapter import Adapter
from miniagent.message_sender import TracingKafkaProducer


class KafkaProducerAdapter(Adapter):

    producer = None

    def __init__(self):
        self.producer = TracingKafkaProducer()

    def produce_message(self, topic: str, message: dict) -> tuple[int, dict]:
        self.producer.send(topic,message)
        return 1, {'message':'OK'}
    
    def __del__(self):
        print('del KafkaProducerAdapter')
        if self.producer:
            self.producer.close()

    def get_status(self) -> int:
        return 1