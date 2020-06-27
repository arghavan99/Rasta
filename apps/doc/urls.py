from django.conf.urls import url
from django.urls import path, include
from apps.doc import views


app_name = "doc"
urlpatterns = [
    path('download/<int:id>/', views.doc_downloader),
]