from django.shortcuts import render
from apps.intro.models import *


def homepage(req):
    upcoming_event = UpcomingEvent.objects.filter(show_on_homepage=True)
    if len(upcoming_event) > 0:
        context = {'upcoming_event': upcoming_event.last()}
    else:
        context = {}
    homepage_data = HomepageData.objects.last()
    link = homepage_data.video_url.split('/')
    url = 'https://www.aparat.com/video/video/embed/videohash/' + str(link[-1]) + '/vt/frame'
    context.update({'intro': homepage_data.intro,
                    'aparat_url': url})
    return render(req, 'intro/index.html', context)

