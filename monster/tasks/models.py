from mongoengine import Document, StringField, DateTimeField
from datetime import datetime


class Task(Document):
    STATUS_CHOICES = ("todo", "in_progress", "done")

    title = StringField(required = True, max_length = 200)
    description = StringField()
    status = StringField(
        required = True,
        choices = STATUS_CHOICES,
        default = "todo"
    )
    created_at = DateTimeField(default = datetime.utcnow)

    meta = {
        "collection": "tasks",
        "ordering": ["-created_at"]
    }
