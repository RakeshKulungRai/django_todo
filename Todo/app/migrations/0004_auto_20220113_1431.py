# Generated by Django 2.2.24 on 2022-01-13 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220104_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.TimeField(default=datetime.time(14, 31, 14, 79207)),
        ),
    ]
