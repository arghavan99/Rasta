from django.urls import path, include

from apps.newsletter import views

app_name = "newsletter"
urlpatterns = [
    path('unsubscribe/<slug:uid>/', views.unsubscribe),
]