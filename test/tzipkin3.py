from flask import Flask, request
import requests
from f_zipkin import Zipkin

app = Flask(__name__)

zipkin = Zipkin(app, sample_rate=10)
#app.config['ZIPKIN_DSN'] = "http://127.0.0.1:9411/api/v2/spans"
app.config['ZIPKIN_ADDRESS']=('localhost',9411)


@app.route('/')
def hello():
    zipkin.update_tags(id='2',shared=False)
    return "Hello from server 3"

if __name__ == "__main__":
    app.run(port=8833)