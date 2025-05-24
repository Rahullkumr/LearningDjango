from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    pname=models.CharField(max_length=100)
    pdesc=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    pcategory=models.CharField(max_length=50)
    trending=models.BooleanField(default=False)
    offer=models.BooleanField(default=False)
    pimages=models.ImageField('Default.jpg',upload_to='uploads')



class CartModel(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    pcategory=models.CharField(max_length=50)
    quatity=models.IntegerField(default=1)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
