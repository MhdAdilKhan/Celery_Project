from celery import schedules
from celery.schedules import crontab
from django.shortcuts import render,HttpResponse
from pytz import HOUR
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask,CrontabSchedule
# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")
def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Email Has Been Sent To Your Registered Email Address!")

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour=15, minute=3)
    task = PeriodicTask.objects.create(crontab=schedule,name = "schedule_mail_task"+"1",task = 'send_mail_app.tasks.send_mail_func')
    return HttpResponse("Done")