from __future__ import absolute_import, unicode_literals

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels.settings')

app = Celery('channels')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


from celery import shared_task

@shared_task
def add(x,y):
    return x+y