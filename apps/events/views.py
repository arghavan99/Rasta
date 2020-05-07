from django.shortcuts import render
from apps.events.models import *


def get_events(request):
    context = {}
    events = Event.objects.order_by('-date')
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


def get_single_event(request, eve_id):
    try:
        event = Event.objects.get(id=eve_id)
    except Event.DoesNotExist:
        response = render(request, 'base/404.html')
        response.status_code = 404
        return response
    docs = Document.objects.filter(event=event)
    context = {
        'event': event,
        'year': event.get_persian_year(),
        'month': event.get_persian_month(),
        'docs': list(docs),
    }
    return render(request, 'events/single_event.html', context)

