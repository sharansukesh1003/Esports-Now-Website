# Generated by Django 3.2.5 on 2021-08-03 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecarousel',
            name='carousel_item',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 22, 12, 47, 910001)),
        ),
    ]