# Generated by Django 5.1.7 on 2025-04-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_demo', '0002_article_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='country',
            field=models.BooleanField(default=0),
        ),
    ]
