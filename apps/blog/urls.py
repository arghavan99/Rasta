from django.conf.urls import url
from django.urls import path, include
from apps.blog import views


app_name = "blog"
urlpatterns = [
    path('<slug:cat_url>/', views.get_posts),
    url(r'^$', views.get_all_posts),
]