# Generated by Django 3.2.5 on 2021-08-03 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_auto_20210803_2217'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepageartcile',
            options={'ordering': ['-date_time']},
        ),
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 3, 22, 47, 40, 671638)),
        ),
    ]