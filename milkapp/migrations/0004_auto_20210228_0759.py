# Generated by Django 3.1.5 on 2021-02-28 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milkapp', '0003_auto_20210228_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='timing',
            field=models.TimeField(default=datetime.time(7, 59, 7, 207431)),
        ),
    ]
