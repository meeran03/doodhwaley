# Generated by Django 3.1.5 on 2021-03-01 06:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milkapp', '0013_auto_20210301_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='timing',
            field=models.TimeField(default=datetime.time(6, 28, 27, 584785)),
        ),
    ]
