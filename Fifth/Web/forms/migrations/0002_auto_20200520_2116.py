# Generated by Django 3.0.6 on 2020-05-20 18:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='commissioner2',
        ),
        migrations.RemoveField(
            model_name='form',
            name='commissioner3',
        ),
        migrations.RemoveField(
            model_name='form',
            name='commissioner4',
        ),
        migrations.RemoveField(
            model_name='form',
            name='supreme_commissioner',
        ),
        migrations.AddField(
            model_name='form',
            name='commissioners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
