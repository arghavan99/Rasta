from django.contrib import admin
from apps.blog.models import *


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


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    fields = ['author_name', 'email', 'text', 'date_time', 'show', 'is_admin_reply', 'comment']


class ReplyInline(admin.TabularInline):
    model = Reply


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author_name', 'email', 'text', 'date_time', 'show', 'post']
    inlines = [
        ReplyInline
    ]
