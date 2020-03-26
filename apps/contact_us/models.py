from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


# Create your models here.


class RastaMember(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    education = models.CharField(max_length=200, blank=False, null=False)
    role = models.CharField(max_length=100, blank=True, null=True)
    photo = models.ImageField(null=False, blank=False)


class UserFeedback(models.Model):
    type_choices = (('student', _('student')),
                    ('teacher', _('teacher')),
                    ('parent', _('parent')))
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=200, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    type = models.CharField(max_length=200, null=False, blank=False, choices=type_choices)
