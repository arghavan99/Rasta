from django.shortcuts import render

from apps.blog.models import BlogPost
from apps.intro.models import *
from apps.events.models import Event
from django import forms
from django.db import IntegrityError
from apps.newsletter.models import Subscriber
from django.http import JsonResponse

def homepage(req):
    get_last_events()
    upcoming_event = UpcomingEvent.objects.filter(show_on_homepage=True)
    if len(upcoming_event) > 0:
        context = {'upcoming_event': upcoming_event.last()}
        # context = {}
    else:
        context = {}
    homepage_data = HomepageData.objects.last()
    if homepage_data is not None:
        link = homepage_data.video_url.split('/')
        url = 'https://www.aparat.com/video/video/embed/videohash/' + str(link[-1]) + '/vt/frame'
        context.update({'aparat_url': url,
                        'intro': homepage_data.intro})
    context.update({'events': get_last_events(),
                    'posts': get_last_blog_posts()})
    return render(req, 'intro/index.html', context)


def get_last_events():
    events = Event.objects.order_by('-date')[:3]
    return [
        {
            'id': event.id,
            'name': event.name,
            'poster': event.poster,
            'year': event.get_persian_year(),
            'month': event.get_persian_month(),
            'summary': event.summary,
            'location': event.location
        } for event in events
    ]


def get_last_blog_posts():
    posts = BlogPost.objects.order_by('-publish_date')[:3]
    return [
        {
            'id': post.id,
            'title': post.title,
            'summary': post.summary,
        } for post in posts
    ]
def notify(request):
    if request.POST:
        valid = True
        try:
            forms.EmailField().clean(request.POST['email'])
        except Exception as e:
            valid = False
        if valid:
            try:
                Subscriber.objects.create(email=request.POST['email'])
            except IntegrityError:
                return JsonResponse({'success': False})
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})