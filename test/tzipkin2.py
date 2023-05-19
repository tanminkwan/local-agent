from flask import Flask, request
import requests
from f_zipkin import Zipkin
from py_zipkin.util import ZipkinAttrs
import inspect

app = Flask(__name__)

zipkin = Zipkin(app, sample_rate=10)
#app.config['ZIPKIN_DSN'] = "http://127.0.0.1:9411/api/v2/spans"
app.config['ZIPKIN_ADDRESS']=('localhost',9411)

"""
with app.app_context():
    zipkin.create_span("pure_app_span")
    z = zipkin.get_zipkin_attrs()
    zipkin.update_tags(status="started")
    with app.app_context():
        zipkin.create_span("child_app_span", trace_id=z.trace_id, parent_span_id=z.span_id)
        z1 = zipkin.get_zipkin_attrs()
        with app.app_context():
            print('# 3 : ',inspect.currentframe().f_code.co_name)
            zipkin.create_span("grandchild_app_span", trace_id=z1.trace_id, parent_span_id=z1.span_id)
"""

@app.route('/')
def hello():
    headers = {}
    zipkin.update_tags(url=request.full_path)
    headers.update(zipkin.create_http_headers_for_new_span())
    #zipkin.update_tags(id='1')
    z0 = zipkin.get_zipkin_attrs()
    with app.app_context():
        print('# 1 : ',inspect.currentframe().f_code.co_name)
        zipkin.create_span("app_span", trace_id=z0.trace_id, parent_span_id=z0.span_id)
        z = zipkin.get_zipkin_attrs()
        zipkin.update_tags(status="started")
        with app.app_context():
            print('# 2 : ',inspect.currentframe().f_code.co_name)
            zipkin.create_span("child_app_span", trace_id=z.trace_id, parent_span_id=z.span_id)
            z1 = zipkin.get_zipkin_attrs()
            with app.app_context():
                zipkin.create_span("grandchild_app_span", trace_id=z1.trace_id, parent_span_id=z1.span_id)
    
    print("$$$$$")
    r = requests.get('http://localhost:8833', headers=headers)
    return r.text

if __name__ == "__main__":
    app.run(port=8832)