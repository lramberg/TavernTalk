# Generated by Django 2.2 on 2019-06-14 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20190614_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 14, 23, 26, 48, 639787), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 14, 23, 26, 48, 641792), verbose_name='Date'),
        ),
    ]
