from django.shortcuts import render
from apps.intro.models import *
from apps.events.models import Event


def homepage(req):
    get_last_events()
    upcoming_event = UpcomingEvent.objects.filter(show_on_homepage=True)
    if len(upcoming_event) > 0:
        context = {'upcoming_event': upcoming_event.last()}
    else:
        context = {}
    homepage_data = HomepageData.objects.last()
    link = homepage_data.video_url.split('/')
    url = 'https://www.aparat.com/video/video/embed/videohash/' + str(link[-1]) + '/vt/frame'
    context.update({'intro': homepage_data.intro,
                    'aparat_url': url,
                    'events': get_last_events()})
    return render(req, 'intro/index.html', context)


def get_last_events():
    return Event.objects.order_by('-date')[:3]
