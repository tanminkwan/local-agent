import sys
import threading
from flask import Flask
from flask_api import status
from flask_apscheduler import APScheduler
from tappender import appender

CNT = 0

def scheduler_test():
    print('scheduler_test called')

def run_flask_app():

    app = Flask(__name__)

    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.add_job(func=scheduler_test, id='scheduler_test', trigger='interval', minutes=1)
    scheduler.start()
    
    @app.get('/')
    def hello():
        global CNT
        CNT += 1
        
        appender.printUrJob('CNT : '+str(CNT))

        if CNT % 5 != 0:
            return "No Way!!", status.HTTP_404_NOT_FOUND
        else:
            return "Hello, world!", status.HTTP_200_OK 

#    __flask = lambda: app.run(host="0.0.0.0", port=8808, debug=True, use_reloader=False)

#    thread = threading.Thread(target=__flask)
#    thread.name = '__flask'
#    thread.start()

    app.run(host="0.0.0.0", port=8808, debug=True, use_reloader=False)

if __name__ == '__main__':
    run_flask_app()
    print('printed?')