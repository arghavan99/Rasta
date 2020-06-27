from django.conf.urls import url
from django.urls import path, include
from apps.intro import views


app_name = "intro"
urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^notify$', views.notify),
]