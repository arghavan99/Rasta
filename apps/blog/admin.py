from django.contrib import admin
from apps.blog.models import BlogPost, Category


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'publish_date', 'photo', 'summary', 'text', 'categories']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'url']
