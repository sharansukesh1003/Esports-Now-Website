# Generated by Django 3.2.5 on 2021-07-28 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageArtcile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=256)),
                ('description', models.TextField(max_length=256)),
                ('image_url', models.ImageField(upload_to='')),
                ('category', models.TextField(max_length=15)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2021, 7, 29, 0, 24, 9, 421857))),
                ('article_link', models.URLField()),
            ],
        ),
    ]
