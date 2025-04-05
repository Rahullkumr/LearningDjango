from django.contrib import admin
from models_demo.models import Article

# Register your models here.


class Articleadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc']

    list_display_links = ['title']
    # to see the Recent actions


admin.site.register(Article, Articleadmin)
