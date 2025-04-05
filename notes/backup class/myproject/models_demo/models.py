from django.db import models

# Create your models here.
# creating model


class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=300)
    # state = models.BooleanField(default=0)
    # country = models.BooleanField(default=0)
