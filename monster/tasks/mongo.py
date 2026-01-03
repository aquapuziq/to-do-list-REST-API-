from mongoengine import connect
from django.conf import settings

_connected = False

def init_mongo():
    global _connected
    if not _connected:
        connect(host = settings.MONGO_URI)
        _connected = True
