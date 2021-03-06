# Generated by Django 3.2.5 on 2021-07-29 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_homepageartcile_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageCarousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=256)),
                ('description', models.TextField(max_length=256)),
                ('image_url', models.URLField()),
                ('category', models.TextField(max_length=15)),
                ('article_link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='homepageartcile',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 29, 22, 58, 11, 530610)),
        ),
    ]
