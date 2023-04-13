import sys
import threading
from flask import Flask
from flask_api import status

CNT = 0
def run_flask_app():
    app = Flask(__name__)

    @app.get('/')
    def hello():
        global CNT
        CNT += 1
        print('CNT : ',CNT)
        if CNT % 5 != 0:
            return "f2 No Way!!", status.HTTP_404_NOT_FOUND
        else:
            return "f2 Hello, world!", status.HTTP_200_OK

    threading.Thread(target=lambda: app.run(host="0.0.0.0", port=8809, debug=True, use_reloader=False)).start()

if __name__ == '__main__':
    run_flask_app()
    print('printed?')