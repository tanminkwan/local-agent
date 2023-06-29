from flask import Flask, request
import requests
from f_zipkin import Zipkin, child_zipkin_span, child_span
from py_zipkin.util import ZipkinAttrs
import inspect

app = Flask(__name__)

zipkin = Zipkin(app, sample_rate=100)
#app.config['ZIPKIN_DSN'] = "http://127.0.0.1:9411/api/v2/spans"
app.config['ZIPKIN_ADDRESS']=('localhost',9411)

@child_span
def deco_test(str_param):
    return {"function_name":"deco_test"}

"""
with child_zipkin_span('span_TEST') as span:
    span.update_tags(status="started")
    with child_zipkin_span('child_span_TEST') as child_span:
        #child_span.update_binary_annotations({'test':'OKKKK'})
        child_span.update_tags(status2="started")
    deco_test("Hello.Hello!!")
"""

#deco_test("MeMeMe!!")

@app.route('/')
def hello():
    
    with child_zipkin_span('span_TEST') as span:
        span.update_tags(status="started")
        deco_test("Hello.Hello!!")
        
    return 'OK'

if __name__ == "__main__":

    app.run(port=8835)