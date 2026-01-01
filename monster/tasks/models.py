from djongo import models

class Task(models.Model):
    STATUS = (
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length = 300)
    description = models.TextField(blank = True)
    status = models.CharField(max_length = 20, choices=STATUS)
