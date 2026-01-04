from pathlib import Path
from mongoengine import connect
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "django_prometheus",
    "tasks",
]

# MONGO_CLIENT = MongoClient("mongodb://localhost:27017")
# MONGO_DB = MONGO_CLIENT["tododb"]
# TASKS_COLLECTION = MONGO_DB["tasks"]

MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "ToDoListAPI_Django.urls"
WSGI_APPLICATION = "ToDoListAPI_Django.wsgi.application"

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb://mongo:27017/tododb"
)

connect(
    host=MONGO_URI,
    uuidRepresentation="standard"
)

REDIS_URL = os.getenv(
    "REDIS_URL",
    "redis://redis:6379/0"
)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
}
