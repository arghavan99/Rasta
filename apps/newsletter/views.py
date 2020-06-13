from django.shortcuts import render

# Create your views here.
from apps.newsletter.models import Subscriber


def unsubscribe(request, uid):
    try:
        s = Subscriber.objects.get(unique_id=uid)
    except Subscriber.DoesNotExist:
        response = render(request, 'base/404.html')
        response.status_code = 404
        return response
    s.delete()
    return render(request, 'newsletter/unsubscribe.html')
