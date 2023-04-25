from datetime import datetime, timedelta
from . import scheduler
from .executer import ExecuterCaller

"""
def printHearBeat():
    print('Thump2!! Thump2!!')

scheduler.add_job(
    trigger='interval',
    id='heartbeat2', 
    name='Heart Beat Check 2',
    minutes=1,
    start_date=datetime.now()+timedelta(minutes=1),
    func=ExecuterCaller.instance().execute_command,
    args=[{'executer':'addin.executer.scheduler.DeviceHealth'}]
)

@scheduler.task('cron', id='heartbeat', name='Heart Beat Check', minute='*/1')
def heartbeat():
    print('Thump!! Thump!!')

"""
class ScheduledJob:
    
    def __init__(self, jobs: list) -> None:

        for job in jobs:
            self._run_job(job)

    def _run_job(self, job: dict) -> int:

        executer = job.pop('executer')
        scheduler.add_job(
            func=ExecuterCaller.instance().execute_command,
            args=[{'executer':executer}],
            **job
        )        
        return 1