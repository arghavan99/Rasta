from django.contrib import admin
from apps.contact_us.models import *


@admin.register(RastaMember)
class MemberAdmin(admin.ModelAdmin):
    fields = ['name', 'education', 'role', 'photo_visible', 'photo_hidden']


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    fields = ['name', 'text', 'email', 'type']
