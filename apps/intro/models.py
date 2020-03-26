from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class HomepageData(models.Model):
    intro = RichTextField()
    video_url = models.URLField(null=True, blank=True)
    # logo = models.ImageField(null=True, blank=True)


class UpcomingEvent(models.Model):
    poster = models.ImageField()
    intro = RichTextField()
    sign_up_link = models.URLField(null=True, blank=True)
