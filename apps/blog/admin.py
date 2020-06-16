from django.contrib import admin
from apps.blog.models import *
from apps.blog.models import BlogPost, Category
from apps.doc.admin import DocumentInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'url']


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    fields = ['title', 'photo', 'summary', 'text', 'categories']
    inlines = [
        DocumentInline
    ]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    fields = ['author_name', 'email', 'text', 'show', 'is_admin_reply', 'comment']


class ReplyInline(admin.TabularInline):
    model = Reply


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['author_name', 'email', 'text',  'show', 'post']
    inlines = [
        ReplyInline
    ]
