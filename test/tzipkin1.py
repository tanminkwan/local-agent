from flask import Flask
import requests
from f_zipkin import Zipkin

app = Flask(__name__)

zipkin = Zipkin(app, sample_rate=100)
#app.config['ZIPKIN_DSN'] = "http://127.0.0.1:9411/api/v2/spans"
app.config['ZIPKIN_ADDRESS']=('localhost',9411)

@app.route('/')
def hello():
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    #zipkin.update_tags(id='1')
    print(headers)
    r = requests.get('http://localhost:8832', headers=headers)
    return r.text

if __name__ == "__main__":
    app.run(port=8831)