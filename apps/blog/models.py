from django.db import models
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from Rasta_Web.utils import validate_file_size, validate_image_size


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    objects = jmodels.jManager()
    photo = models.ImageField(upload_to='blog/', null=True, blank=True, validators=[validate_image_size])
    title = models.CharField(max_length=70, null=False, blank=False)
    publish_date = jmodels.jDateTimeField()
    summary = models.TextField(max_length=100, null=False, blank=False)
    text = RichTextField(null=False, blank=False)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_persian_date(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date).translate(translate_table)

    def get_persian_month(self):
        months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
        return months[self.publish_date.month - 1]

    def get_persian_year(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.year).translate(translate_table)

    def get_persian_time(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.time()).translate(translate_table)

    def get_persian_day(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.day).translate(translate_table)



# class BlogDocument(models.Model):
#     caption = models.CharField(max_length=200, null=False, blank=False)
#     file = models.FileField(null=False, blank=False, upload_to='blog_documents/', validators=[validate_file_size])
#     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.post) + ' - ' + str(self.file.name)
#