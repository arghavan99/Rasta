from django.contrib import admin
from apps.intro.models import *


# Register your models here.

@admin.register(HomepageData)
class HomePageAdmin(admin.ModelAdmin):
    fields = ['intro', 'video_url']


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    fields = ['poster', 'intro', 'title', 'button_link', 'button_name']


