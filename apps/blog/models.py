from django.db import models
from django_jalali.db import models as jmodels
from ckeditor.fields import RichTextField
from Rasta_Web.utils import validate_file_size, validate_image_size,validate_square_image


def persian_date(obj):
    translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return str(obj.strftime("%Y-%m-%d %H:%M")).translate(translate_table)


class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    url = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    objects = jmodels.jManager()
    photo = models.ImageField(upload_to='blog/', null=True, blank=True,help_text="این تصویر باید مربعی باشد", validators=[validate_image_size,validate_square_image])
    title = models.CharField(max_length=70, null=False, blank=False)
    publish_date = jmodels.jDateTimeField(auto_now_add=True)
    summary = models.TextField(max_length=100, null=False, blank=False)
    text = RichTextField(null=False, blank=False)
    categories = models.ManyToManyField(Category, related_name='blog_posts')

    def __str__(self):
        return self.title

    def get_persian_date(self):
        return persian_date(self.publish_date)

    def get_persian_month(self):
        months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
        return months[self.publish_date.month - 1]

    def get_persian_year(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.year).translate(translate_table)

    def get_persian_time(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.time().strftime(" %H:%M ")).translate(translate_table)

    def get_persian_day(self):
        translate_table = str.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
        return str(self.publish_date.day).translate(translate_table)



class Comment(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False)
    author_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    date_time = jmodels.jDateTimeField(auto_now_add=True)
    show = models.BooleanField(null=False, blank=False, default=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return 'post number' + str(self.post.id) + ' -  ' + str(self.id)

    def get_persian_date(self):
        return persian_date(self.date_time)


class Reply(models.Model):
    text = models.TextField(max_length=500, null=False, blank=False)
    author_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    date_time = jmodels.jDateTimeField(auto_now_add=True)
    show = models.BooleanField(null=False, blank=False, default=True)
    is_admin_reply = models.BooleanField(null=False, blank=False ,default=False)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return 'post number' + str(self.comment.post.id) + ' - comment ' + str(self.comment.id) + ' - ' + str(self.id)

    def get_persian_date(self):
        return persian_date(self.date_time)
