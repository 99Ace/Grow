# Generated by Django 2.2.4 on 2021-05-07 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20210507_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logrecord',
            name='date',
        ),
        migrations.AddField(
            model_name='logrecord',
            name='log_datetime',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 7, 17, 12, 9, 64172)),
        ),
    ]
