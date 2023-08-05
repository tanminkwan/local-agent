from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job
import threading
import time
from datetime import datetime, timedelta
import os

scheduler = BackgroundScheduler()

def scheduler_test():
    print('scheduler_test called')

def scheduler_once():
    print('scheduler_once called')

def commit_suicide():
    p = [ j.id for j in scheduler.get_jobs() if j.id != 'commit_suicide']
    if not p:
        os._exit(1)

def run_scheduler():
    scheduler.add_job(func=scheduler_once, id='scheduler_once', run_date = datetime.now() + timedelta(minutes=1))
    #scheduler.add_job(func=scheduler_test, id='scheduler_test', trigger='interval', seconds=30)
    scheduler.add_job(func=kill_me, id='kill_me', trigger='interval', seconds=10)
    scheduler.start()

if __name__ == '__main__':
    run_scheduler()
    print('run_scheduler')

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()