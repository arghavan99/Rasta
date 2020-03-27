from django.contrib import admin
from apps.intro.models import *


# Register your models here.

@admin.register(HomepageData)
class HomePageAdmin(admin.ModelAdmin):
    fields = ['intro', 'video_url']


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(admin.ModelAdmin):
    fields = ['poster', 'intro', 'sign_up_link']
