from django.conf import settings
from bson import ObjectId

collection = settings.TASKS_COLLECTION

def get_all():
    tasks = list(collection.find())
    for t in tasks:
        t["id"] = str(t["_id"])
        del t["_id"]
    return tasks

def get_one(task_id):
    task = collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        return None
    task["id"] = str(task["_id"])
    del task["_id"]
    return task

def create(data):
    result = collection.insert_one(data)
    data["id"] = str(result.inserted_id)
    return data

def update(task_id, data):
    collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": data}
    )
    return get_one(task_id)

def delete(task_id):
    collection.delete_one({"_id": ObjectId(task_id)})
