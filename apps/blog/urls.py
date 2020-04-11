from django.conf.urls import url
from django.urls import path, include
from apps.blog import views


app_name = "blog"
urlpatterns = [
    url(r'^$', views.get_posts),
]