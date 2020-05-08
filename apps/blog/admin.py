from django.contrib import admin
from apps.blog.models import BlogPost, Category, BlogDocument


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'url']


@admin.register(BlogDocument)
class BlogDocAdmin(admin.ModelAdmin):
    fields = ['caption', 'file', 'post']


class BlogDocumentInline(admin.TabularInline):
    model = BlogDocument


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'publish_date', 'photo', 'summary', 'text', 'categories']
    inlines = [
        BlogDocumentInline
    ]

