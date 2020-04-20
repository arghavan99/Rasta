from django.db import models
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    objects = jmodels.jManager()
    photo = models.ImageField(upload_to='blog/', null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    publish_date = jmodels.jDateTimeField()
    summary = models.TextField(max_length=100, null=False, blank=False)
    text = RichTextField(null=False, blank=False)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_persian_date(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date).translate(translate_table)
