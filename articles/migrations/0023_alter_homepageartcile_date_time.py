# Generated by Django 3.2.5 on 2021-08-01 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 16, 22, 53, 628275)),
        ),
    ]
