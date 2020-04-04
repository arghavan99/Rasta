from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class HomepageData(models.Model):
    intro = RichTextField()
    video_url = models.URLField(null=True, blank=True)
    # logo = models.ImageField(null=True, blank=True)


class UpcomingEvent(models.Model):
    poster = models.ImageField(null=False, blank=False)
    intro = RichTextField()
    title = RichTextField()
    button_link = models.URLField(null=False, blank=False)
    button_name = models.CharField(null=False, blank=False, max_length=50)
