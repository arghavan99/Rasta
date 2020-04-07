from django.contrib import admin
from apps.intro.models import *


@admin.register(HomepageData)
class HomePageAdmin(admin.ModelAdmin):
    fields = ['intro', 'video_url']


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    fields = ['poster', 'intro', 'title', 'button_link', 'button_name', 'show_on_homepage']
