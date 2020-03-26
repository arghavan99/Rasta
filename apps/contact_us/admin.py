from django.contrib import admin
from apps.contact_us.models import *


# Register your models here.

@admin.register(RastaMember)
class MemberAdmin(admin.ModelAdmin):
    fields = ['name', 'education', 'role', 'photo']


@admin.register(UserFeedback)
class UserFeedbackAdmin(admin.ModelAdmin):
    fields = ['name', 'text', 'email', 'type']
