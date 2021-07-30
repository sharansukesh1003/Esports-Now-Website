from datetime import time
from django.db import models
import datetime

now = datetime.datetime.now()


class HomePageArtcile(models.Model):
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=256)
    image_url = models.URLField()
    category = models.TextField(max_length=15)
    date_time = models.DateTimeField(default=now)
    article_link = models.URLField()

class HomePageCarousel(models.Model):
    title = models.TextField(max_length=256)
    description = models.TextField(max_length=256)
    image_url = models.URLField()
    category = models.TextField(max_length=15)
    article_link = models.URLField()