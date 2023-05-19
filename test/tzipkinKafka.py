from kafka import KafkaProducer
from py_zipkin.encoding import Encoding
from py_zipkin.transport import SimpleHTTPTransport
from py_zipkin.util import generate_random_64bit_string
from py_zipkin.zipkin import zipkin_span, ZipkinAttrs
import json

class TracingKafkaProducer(KafkaProducer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send(self, topic, value=None, key=None, headers=None, partition=None, timestamp_ms=None):

        trace_id = generate_random_64bit_string()
        span_id = generate_random_64bit_string()
        
        zipkin_attrs = ZipkinAttrs(
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=None,
            flags=None,
            is_sampled=True,
        )

        with zipkin_span(
            service_name='my_kafka_producer',
            span_name='kafka_produce',
            zipkin_attrs=zipkin_attrs,
            transport_handler=SimpleHTTPTransport('localhost', 9411),
            #transport_handler=post,
            encoding=Encoding.V2_JSON,
        ) as span:

            return super().send(topic, value=json.dumps(value).encode('utf-8'), key=key, headers=headers, partition=partition, timestamp_ms=timestamp_ms)

# Instantiate the TracingKafkaProducer
producer = TracingKafkaProducer(
    bootstrap_servers=['localhost:9092']
)
message = dict(
                id = 'BLUE_SKUL_NO13',
                age = 35,
                gender = 'F'
            )
producer.send('T_ZIPKIN', value=message)