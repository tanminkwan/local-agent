from kafka import KafkaConsumer
from py_zipkin.zipkin import zipkin_span, ZipkinAttrs
from py_zipkin.util import generate_random_64bit_string
from requests import post
from py_zipkin.encoding import Encoding
from py_zipkin.transport import SimpleHTTPTransport
import json


class hennry_zipkin_span(zipkin_span):

    def __init__(self, *args, **kwargs):

        if not kwargs.get('transport_handler'):
            kwargs.update(transport_handler=SimpleHTTPTransport('localhost', 9411))
        if not kwargs.get('service_name'):
            kwargs.update(service_name='my_consumer_service')
        if not kwargs.get('encoding'):
            kwargs.update(encoding=Encoding.V2_JSON)

        print("kwargs : ", kwargs)
        super().__init__(*args, **kwargs)

# Kafka consumer settings
bootstrap_servers = ['127.0.0.1:9092']
group_id = 'my_consumer_group'
topic = 'T_ZIPKIN'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    group_id=group_id
)

# Consume and process Kafka messages
for message in consumer:
    
    val = json.loads(message.value.decode())
    print('val :', type(val), val)
    #headers = message.headers
    #print('headers : ',headers)
    header = val.get('header')
    content = val.get('message')

    trace_id = header.get('trace_id') if header and header.get('trace_id') else generate_random_64bit_string()
    parent_span_id = header.get('span_id') if header and header.get('span_id') else None
    span_id = generate_random_64bit_string()

    zipkin_attrs = ZipkinAttrs(
        trace_id=trace_id,
        span_id=span_id,
        parent_span_id=parent_span_id,
        flags=None,
        is_sampled=True,
    )
    
    with hennry_zipkin_span(
        #service_name='my_consumer_service',
        span_name='consume_message',
        #transport_handler=SimpleHTTPTransport('localhost', 9411),
        #encoding=Encoding.V2_JSON,
        zipkin_attrs=zipkin_attrs,
    ) as span:
        # Process the Kafka message here
        span.logging_context.tags.update(message=str(content))
        """
        span.add_sa_binary_annotation('abc','123')
        span.add_sa_binary_annotation('message',str(val))
        """
        print(f'Received message: {message.value.decode()}')
