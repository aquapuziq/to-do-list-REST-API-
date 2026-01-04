from .models import Task
from mongoengine.errors import DoesNotExist


def get_all():
    return [
        {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "status": task.status,
            #"created_at": task.created_at,
        }
        for task in Task.objects.all()
    ]


def get_one(task_id):
    try:
        task = Task.objects.get(id = task_id)
    except DoesNotExist:
        return None

    return {
        "id": str(task.id),
        "title": task.title,
        "description": task.description,
        "status": task.status,
        #"created_at": task.created_at,
    }


def create(data):
    task = Task(**data)
    task.save()

    return {
        "id": str(task.id),
        "title": task.title,
        "description": task.description,
        "status": task.status,
        #"created_at": task.created_at,
    }


def update(task_id, data):
    try:
        task = Task.objects.get(id = task_id)
    except DoesNotExist:
        return None

    for field, value in data.items():
        setattr(task, field, value)

    task.save()
    return get_one(task_id)


def delete(task_id):
    try:
        task = Task.objects.get(id = task_id)
        task.delete()
        return True
    except DoesNotExist:
        return False
