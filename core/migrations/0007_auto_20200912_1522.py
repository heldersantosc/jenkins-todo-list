# Generated by Django 2.1.7 on 2020-09-12 18:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200912_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 12, 15, 22, 22, 562433)),
        ),
    ]