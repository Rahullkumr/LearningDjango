from django.db import models

# Create your models here.


class StudentModel(models.Model):
    sname = models.CharField(max_length=50)
    srollno = models.IntegerField()
    course = models.CharField(max_length=50)
