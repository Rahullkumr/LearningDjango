from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    course = models.CharField(max_length=100)
