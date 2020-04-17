from django.conf.urls import url
from django.urls import path, include
from apps.events import views


app_name = "events"
urlpatterns = [
    url(r'^$', views.get_events),
]