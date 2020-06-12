from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class EmailText(models.Model):
    subject = models.CharField(null=False, blank=False, max_length=100)
    text = RichTextField(null=False, blank=False, max_length=1000)
    link = models.CharField(null=True, blank=True, max_length=400)
    image = models.ImageField()


class Subscriber(models.Model):
    email = models.EmailField()
    date_joint = models.DateTimeField(auto_now_add=True)
