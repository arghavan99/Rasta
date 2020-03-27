from django.shortcuts import render

# Create your views here.


def homepage(req):
    html = "<html><body>It is now.</body></html>"
    from django.http import HttpResponse
    return HttpResponse(html)