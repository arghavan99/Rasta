from django.conf.urls import url
from django.urls import path, include
from apps.events import views


urlpatterns = [
    path('<int:eve_id>/album/', views.get_photos),
    path('<int:eve_id>/', views.get_single_event),
    url(r'^$', views.get_events),
]
app_name = "events"
