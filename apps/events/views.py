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
    context = {
        'event': event,
        'year': event.get_persian_year(),
        'month': event.get_persian_month(),
        'docs': get_docs(event),
    }
    return render(request, 'events/single_event.html', context)


def get_photos(request, eve_id):
    try:
        event = Event.objects.get(id=eve_id)
    except Event.DoesNotExist:
        response = render(request, 'base/404.html')
        response.status_code = 404
        return response
    photos = EventPhoto.objects.filter(event=event)
    context = {
        'event_name': event.name,
        'photos': list(photos)
    }
    return render(request, 'events/album.html', context)


def get_docs(event):
    docs = Document.objects.filter(event=event)
    return [(doc, get_doc_type(doc)) for doc in docs]


def get_doc_type(doc):
    # ext = doc.file.name.split('.')[1]
    # if ext in ['png', 'jpg', 'jpeg']:
    #     return 'img'
    # if ext in ['doc', 'docs']:
    #     return 'doc'
    # if ext in ['xlsx', 'xls', 'csv']:
    #     return 'xlsx'
    # if ext in ['pdf']:
    #     return ext
    # return 'txt'
    return 'pdf'
