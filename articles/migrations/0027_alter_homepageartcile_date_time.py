# Generated by Django 3.2.5 on 2021-08-02 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20210802_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 2, 22, 44, 36, 511338)),
        ),
    ]
