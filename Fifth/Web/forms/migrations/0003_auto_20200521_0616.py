# Generated by Django 3.0.6 on 2020-05-21 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20200520_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='act_date',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='good',
            name='form',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='forms.Form'),
        ),
    ]
