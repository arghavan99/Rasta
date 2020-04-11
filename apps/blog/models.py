from django.db import models
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    objects = jmodels.jManager()
    photo = models.ImageField(upload_to='blog/', null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    publish_date = jmodels.jDateTimeField()
    summary = models.TextField(max_length=300, null=True, blank=True)
    text = RichTextField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    def __str__(self):
        return self.title



