import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ToDoListAPI_Django.settings')

app = Celery('ToDoListAPI_Django')
app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()
