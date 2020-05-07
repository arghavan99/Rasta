from django.conf.urls import url
from django.urls import path, include
from apps.events import views


app_name = "events"
urlpatterns = [
    path('<int:eve_id>/', views.get_single_event),
    url(r'^$', views.get_events),
]