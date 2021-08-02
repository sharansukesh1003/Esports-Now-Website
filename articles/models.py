from django.db import models
import datetime

now = datetime.datetime.now()

class HomePageArtcile(models.Model):
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=256)
    image_url = models.URLField()
    category = models.TextField(max_length=15)
    date_time = models.DateTimeField(default=now)
    article = models.TextField(max_length=4000,default='empty')

class HomePageCarousel(models.Model):
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=256)
    image_url = models.URLField()
    category = models.TextField(max_length=15)
    article = models.TextField(max_length=4000,default='empty')
