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
            'year': event.date.year,
            'month': event.date.month,
            'summary': event.summary
        } for event in events]
    print(context)
    return render(request, 'events/events.html', context)

