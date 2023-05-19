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

        #new_headers = []
            
        trace_id = headers.get('trace_id') if headers and headers.get('trace_id') \
                        else generate_random_64bit_string()
        #new_headers.append(('trace_id',trace_id.encode('utf-8')))
        
        span_id = headers.get('span_id') if headers and headers.get('span_id') \
                        else generate_random_64bit_string()
        #new_headers.append(('span_id',span_id.encode('utf-8')))
        
        parent_span_id=None
        if headers and headers.get('parent_span_id'):
            parent_span_id=headers.get('parent_span_id')
            #new_headers.append(('parent_span_id',parent_span_id.encode('utf-8')))

        flags=None
        if headers and headers.get('flags'):
            flags=headers.get('flags')
            #new_headers.append(('flags',str(flags).lower().encode('utf-8')))

        #new_headers.append(('is_sampled',b'1'))

        zipkin_attrs = ZipkinAttrs(
            trace_id=trace_id,
            span_id=span_id,
            parent_span_id=parent_span_id,
            flags=flags,
            is_sampled=True,
        )

        new_headers = dict(
            trace_id=trace_id,
            span_id=span_id,
            flags=flags if flags else '0',
            is_sampled='1',
        )
        if parent_span_id:
            new_headers.update({'parent_span_id':parent_span_id})

        new_value = {'message':value,'header':new_headers}

        with zipkin_span(
            service_name='my_kafka_producer',
            span_name='kafka_produce',
            zipkin_attrs=zipkin_attrs,
            transport_handler=SimpleHTTPTransport('localhost', 9411),
            encoding=Encoding.V2_JSON,
        ) as span:
            span.logging_context.tags.update(message=new_value)
        
            return super().send(topic, value=json.dumps(new_value).encode('utf-8'), key=key, headers=None, partition=partition, timestamp_ms=timestamp_ms)

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