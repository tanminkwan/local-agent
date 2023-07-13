from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import json
import logging
import threading
from time import sleep
import sys
        
class MessageReceiver:

    def __init__(self, bootstrap_servers: list, group_id: str, topics: list, event: threading.Event) -> None:

        self.event = event
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        self.consumer = None
        try:
            consumer = KafkaConsumer(
                                bootstrap_servers=bootstrap_servers,
                                auto_offset_reset='earliest',
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                group_id=group_id,
                            )
            self.consumer = consumer
        except NoBrokersAvailable as e:
            logging.warning('## No Kafka Brokers Available.')
            pass
            #return
        
        self.topics = topics
        #self.consumer.subscribe(self.topics)
        self._start_polling()

    def get_thread(self):
        return self.thread
    
    def _get_consumer_handle(self):
        try:
            consumer = KafkaConsumer(
                                bootstrap_servers=self.bootstrap_servers,
                                auto_offset_reset='earliest',
                                value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                group_id=self.group_id,
                            )
        except NoBrokersAvailable as e:
            logging.warning('No Kafka Brokers Available.')
            return None
        return consumer        

    def _polling(self):

        while not self.consumer:
            self.consumer = self._get_consumer_handle()
            sleep(10)
        
        self.consumer.subscribe(self.topics)

        while True:

            if self.event.is_set():
                logging.warning('MessageReceiver is broken.')
                break

            try:
                results = self.consumer.poll(10.0)
            except Exception as e:
                print('Exception : ', e.__str__)
                sleep(10)
                continue

            if not results:
                sleep(5)
            
            for topic_partition, messages in results.items():
                for message in messages:
                    print(message.value)

    def _start_polling(self):

        self.thread = threading.Thread(target=self._polling)
        self.thread.name = '_kafka_consumer'
        self.thread.start()
    
    def __del__(self):
        #if self.consumer:
        #    self.consumer.close()
        try:
            self.consumer.close()
        except Exception as e:
            pass

if __name__ == '__main__':
    stop_event = threading.Event()

    def signal_handler(sig, frame):
        global stop_event
        stop_event.set()
        sys.stderr.write("KeyboardInterrupt received, stopping...\n")
        sys.exit(0)

    MessageReceiver(
        group_id = 'raffle',
        bootstrap_servers = ['localhost:9092'],
        topics = ['deposit.raffle'],
        event = stop_event
    )