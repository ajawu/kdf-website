import os
# from __future__ import absolute_import, unicode_literals
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kdf.settings')

app = Celery('kdf')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

