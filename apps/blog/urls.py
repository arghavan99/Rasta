from django.conf.urls import url
from django.urls import path, include
from apps.blog import views


app_name = "blog"
urlpatterns = [
    path('posts/<int:post_id>/<str:rest>/', views.get_single_post),
    path('submit_c_r/', views.submit_comment_reply, name='submit_comment_reply'),
    path('<slug:cat_url>/', views.get_posts),
    url(r'^$', views.get_all_posts),
]