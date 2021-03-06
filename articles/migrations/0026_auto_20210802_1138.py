# Generated by Django 3.2.5 on 2021-08-02 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageartcile',
            name='article',
            field=models.TextField(default='empty', max_length=4000),
        ),
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 2, 11, 38, 46, 139904)),
        ),
        migrations.AlterField(
            model_name='homepagecarousel',
            name='article',
            field=models.TextField(default='empty', max_length=4000),
        ),
    ]
