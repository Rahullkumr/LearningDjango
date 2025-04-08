from django.db import models

# Create your models here.


class Tasks(models.Model):
    task_todo = models.TextField()
