from django.contrib import admin

# Register your models here.

from .models import Products


class Productadmin(admin.ModelAdmin):
    list_display=['id','pname','pcategory']

admin.site.register(Products,Productadmin)