from apscheduler.schedulers.blocking import BlockingScheduler
from app import updateDBstock, updateDBtwits
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=10)
def timed_job1():
    updateDBstock()
    print('stock price is updated every 10 minutes.')


@sched.scheduled_job('interval', minutes=30)
def timed_job2():
    updateDBtwits()
    print('stock twits is updated every 30 minutes.')


@sched.scheduled_job('cron', day_of_week='mon-fri', hour='9.5-16')
def scheduled_job():
    timed_job1()
    timed_job2()
    print('This job is run every weekday at 9:30 to 16.')

sched.start()
