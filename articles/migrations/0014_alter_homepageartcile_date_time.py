# Generated by Django 3.2.5 on 2021-07-30 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 30, 11, 36, 59, 820842)),
        ),
    ]
