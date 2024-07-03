from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import register_events, DjangoJobStore
from .views import wordPost



def start():
    scheduler=BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')
    register_events(scheduler)
    @scheduler.scheduled_job('cron', hour=17, minute=23, second=59, name = 'wordPost')
    def auto_wordPost():
        wordPost()
    scheduler.start()