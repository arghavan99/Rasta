from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from apps.doc.models import *


class DocumentInline(GenericTabularInline):
    model = Document
