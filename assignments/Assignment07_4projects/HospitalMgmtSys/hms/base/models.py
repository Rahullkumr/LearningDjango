from django.db import models

# Create your models here.


class Patient(models.Model):

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    aadhaar = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    health_problem = models.TextField()
    date_of_visit = models.CharField(max_length=10)
