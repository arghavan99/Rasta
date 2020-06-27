from django import forms

from apps.blog.models import Comment, Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'email', 'text', 'post']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['author_name', 'email', 'text', 'comment']
