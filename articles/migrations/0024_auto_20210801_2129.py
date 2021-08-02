# Generated by Django 3.2.5 on 2021-08-01 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepageartcile',
            name='article_link',
        ),
        migrations.RemoveField(
            model_name='homepagecarousel',
            name='article_link',
        ),
        migrations.AddField(
            model_name='homepageartcile',
            name='article',
            field=models.TextField(default='empty', max_length=2000),
        ),
        migrations.AddField(
            model_name='homepagecarousel',
            name='article',
            field=models.TextField(default='empty', max_length=2000),
        ),
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 1, 21, 29, 58, 100330)),
        ),
    ]