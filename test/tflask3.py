from flask import Flask, request, current_app
from flask_request_id_header import middleware
from flask_request_id_header.middleware import RequestID
import requests
from flask import g
from uuid import UUID, uuid4

from flask_zipkin import Zipkin

class Hello(object):

    uuid = None

    def __init__(self, app=None):
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None

    def init_app(self, app):
        app.config.setdefault('REQUEST_ID', 'AAAAA')
        
        if hasattr(app, 'before_request'):
            app.before_request(self._before_request)

        if hasattr(app, 'teardown_appcontext'):
            print('[T]teardown_appcontext in app')
            app.teardown_appcontext(self.teardown)
        else:
            print('[T]teardown_appcontext not in app')
            app.teardown_request(self.teardown)

    def _before_request(self):
        print('[T]before_request is called bye!! ')

    def teardown(self, exception):
        print('[T]teardown is called bye!! ')

    def hello(self):
        print('[T]Hello!! ', g.uuid )

    @property
    def sayhello(self):
        g.uuid = str(uuid4())
        if 'hello' not in g:
            g.hello = self.hello()
        return g.hello    

app = Flask(__name__)

app.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'FOO-'

RequestID(app)

talk = Hello(app)

zipkin = Zipkin(app, sample_rate=10)
app.config['ZIPKIN_DSN'] = "http://127.0.0.1:9411/api/v1/spans"

@app.route('/')
def hello_world():

    print(request.environ.get("HTTP_X_REQUEST_ID"))

    print ('OUT ###')
    print (talk.sayhello)
    
    with app.app_context():
        print ('IN ###')
        print (talk.sayhello)

    return 'hello world'

@app.route('/zipkin')
def t_zipkin():
    headers = {}

    headers.update(zipkin.create_http_headers_for_new_span())
    r = requests.get('http://localhost:8809', headers=headers)
    return r.text

if __name__ == '__main__':

    #with app.app_context():
        # within this block, current_app points to app.
    #    print ('OUT ###')
    #    print (talk.sayhello)

    app.run(host="0.0.0.0", port=8808, debug=True, use_reloader=False)
