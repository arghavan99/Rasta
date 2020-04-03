from django.shortcuts import render

# Create your views here.
from apps.intro.models import *


def homepage(req):
    upcoming_event = UpcomingEvent.objects.last()
    homepage_data = HomepageData.objects.last()
    link = homepage_data.video_url.split('/')
    url = 'https://www.aparat.com/video/video/embed/videohash/' + str(link[-1]) + '/vt/frame'
    context = {'intro': homepage_data.intro,
               'aparat_url': url,
               'upcoming_event': upcoming_event}
    return render(req, 'intro/index.html', context)