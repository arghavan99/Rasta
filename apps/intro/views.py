from django.shortcuts import render

# Create your views here.
from apps.intro.models import *


def homepage(req):
    upcoming_event = UpcomingEvent.objects.last()
    homepage_data = HomepageData.objects.last()
    context = {'homepage_data': homepage_data,
               'upcoming_event': upcoming_event}
    return render(req, 'intro/index.html', context)