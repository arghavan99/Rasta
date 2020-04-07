from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class RastaMember(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    education = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=100, blank=True, null=True)
    photo_visible = models.ImageField(null=False, blank=False)
    photo_hidden = models.ImageField(null=False, blank=False)

    def save(self):
        im1 = Image.open(self.photo_visible)
        im2 = Image.open(self.photo_hidden)
        output1 = BytesIO()
        output2 = BytesIO()
        im1 = im1.resize((150, 150))
        im2 = im2.resize((150, 150))
        im1.save(output1, format='png', quality=100)
        im2.save(output2, format='png', quality=100)
        output1.seek(0)
        output2.seek(0)
        self.photo_visible = InMemoryUploadedFile(output1, 'ImageField',
                                                  "%s.jpg" % self.photo_visible.name.split('.')[0], 'image/jpeg',
                                                  sys.getsizeof(output1), None)
        self.photo_hidden = InMemoryUploadedFile(output2, 'ImageField', "%s.jpg" % self.photo_hidden.name.split('.')[0],
                                                 'image/jpeg',
                                                 sys.getsizeof(output2), None)
        super(RastaMember, self).save()

    def __str__(self):
        return self.name + ' - ' + self.role


class UserFeedback(models.Model):
    type_choices = (('student', 'دانش آموز'),
                    ('teacher', 'آموزگار'),
                    ('parent', 'پدر یا مادر'),
                    ('other', 'دیگر'))
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    type = models.CharField(max_length=200, null=False, blank=False, choices=type_choices)
    submit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.submit_time) + ' - ' + self.type
