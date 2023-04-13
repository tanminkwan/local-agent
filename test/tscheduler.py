from apscheduler.schedulers.background import BackgroundScheduler
import threading
import time

scheduler = BackgroundScheduler()

def scheduler_test():
    print('scheduler_test called')

def run_scheduler():
    scheduler.add_job(func=scheduler_test, id='scheduler_test', trigger='interval', seconds=30)
    scheduler.start()

if __name__ == '__main__':
    run_scheduler()
    print('run_scheduler')

    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()