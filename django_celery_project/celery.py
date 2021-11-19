from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from send_mail_app.tasks import send_mail_func

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_celery_project.settings')
app = Celery('django_celery_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace = 'CELERY')

#Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-everyday':{
        'task': 'send_mail_app.tasks.send_mail_func',
        'schedule':crontab(hour=14, minute=32, day_of_month=19,month_of_year=6),
    }
}

app.autodiscover_tasks()
@app.task(bind = True)
def debug_task(self):
    print(f'Request:{self.request!r}')