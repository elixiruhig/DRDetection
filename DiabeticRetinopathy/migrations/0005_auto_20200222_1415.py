# Generated by Django 2.2.1 on 2020-02-22 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DiabeticRetinopathy', '0004_auto_20200222_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 14, 15, 37, 737137)),
        ),
    ]
