from django.shortcuts import render
from apps.events.models import *


def get_events(request):
    context = {}
    events = Event.objects.all()
    context['events'] = [
        {
            'id': event.id,
            'name': event.name,
            'poster': event.poster,
            'year': event.get_persian_year(),
            'month': event.get_persian_month(),
            'summary': event.summary,
            'location': event.location
        } for event in events]


    return render(request, 'events/events.html', context)

