import threading
from tpolling import polling
from tflask import run_flask_app

if __name__ == '__main__':
    #run_scheduler()
    polling('http://localhost:8809')
    run_flask_app()
    for thread in threading.enumerate(): 
        print(thread.name)