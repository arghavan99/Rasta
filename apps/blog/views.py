import json

from django.http import HttpResponse
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

from Rasta_Web.settings.base import bibot_SiteKey
from Rasta_Web.utils import check_bibot_response
from apps.blog.forms import CommentForm, ReplyForm
from apps.blog.models import *
from django.template.loader import render_to_string
from apps.doc.models import Document


def cat_dictionary(cat):
    return {
        'id': cat.id,
        'title': cat.title,
        'url': cat.url
    }


def post_dictionary(post):
    return {
        'id': post.id,
        'title': post.title,
        'photo': post.photo,
        'publish_date': post.get_persian_date(),
        'summary': post.summary,

        'categories': [cat_dictionary(cat) for cat in post.categories.all()]
    }


def single_post_dictionary(post):
    return {
        'id': post.id,
        'title': post.title,
        'photo': post.photo,
        'publish_date': post.get_persian_date(),
        'summary': post.summary,
        'text': post.text,
        'categories': [cat_dictionary(cat) for cat in post.categories.all()]
    }


def reply_dictionary(reply):
    return {
        'text': reply.text,
        'author_name': reply.author_name,
        'email': reply.email,
        'date_time': reply.get_persian_date(),
        'show': reply.show,
        'is_admin': reply.is_admin_reply,
    }


def comment_dictionary(comment):
    return {
        'id': comment.id,
        'text': comment.text,
        'author_name': comment.author_name,
        'email': comment.email,
        'date_time': comment.get_persian_date(),
        'show': comment.show,
        'replies': [reply_dictionary(r) for r in Reply.objects.filter(comment=comment)]
    }


def vis_hid_cats(num, categories):
    if len(categories) <= num + 1:
        context = {
            'vis_cats': [cat_dictionary(cat) for cat in categories],
        }
    else:
        context = {
            'vis_cats': [cat_dictionary(cat) for cat in categories[:num]],
            'hid_cats': [cat_dictionary(cat) for cat in categories[num:]]
        }
    return context


def sort_cats(categories):
    cats = [[cat, len(BlogPost.objects.filter(categories__in=[cat]))] for cat in categories]
    cats = sorted(cats, key=lambda x: x[1], reverse=True)
    res = [c[0] for c in cats]
    return res


def get_all_posts(request):
    categories = Category.objects.all()
    categories = sort_cats(categories)
    posts = BlogPost.objects.order_by('-publish_date')
    context = vis_hid_cats(8, categories)
    context['active_cat'] = ''
    context['posts'] = [post_dictionary(post) for post in posts]
    return render(request, 'blog/blog.html', context)


def get_posts(request, cat_url):
    try:
        active_cat = Category.objects.get(url=cat_url)
    except Category.DoesNotExist:
        response = render(request, 'base/404.html')
        response.status_code = 404
        return response
    categories = Category.objects.exclude(id=active_cat.id)
    categories = sort_cats(categories)
    context = vis_hid_cats(7, categories)
    context['active_cat'] = cat_dictionary(active_cat)
    posts = BlogPost.objects.order_by('-publish_date').filter(categories__in=[active_cat])
    context['posts'] = [post_dictionary(post) for post in posts]
    return render(request, 'blog/blog.html', context)


def get_single_post(request, post_id, rest):
    try:
        post = BlogPost.objects.get(id=post_id)
    except BlogPost.DoesNotExist:
        response = render(request, 'base/404.html')
        response.status_code = 404
        return response
    context = {
        'post': single_post_dictionary(post),
        'comments': [comment_dictionary(com) for com in Comment.objects.filter(post_id=post_id)],
        'docs': get_docs(post),
        'year': post.get_persian_year(),
        'month': post.get_persian_month(),
        'day': post.get_persian_day(),
        'time': post.get_persian_time(),
        'bibot': bibot_SiteKey,
        'reply_form': render_to_string('blog/reply_form.html', {'bibot': bibot_SiteKey}, request),
    }
    return render(request, 'blog/single_post.html', context)


def submit_comment_reply(request):
    response = {}
    if not check_bibot_response(request):
        response['bibot_err'] = 'error'
        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )
    if request.POST['is_comment'] == 'True':
        form = CommentForm(request.POST)
    else:
        form = ReplyForm(request.POST)
    response.update(request.POST)
    if form.is_valid():
        m = form.save()
        if request.POST['is_comment'] == 'True':
            response['comment'] = comment_dictionary(m)
        else:
            response['reply'] = reply_dictionary(m)
        return HttpResponse(
            json.dumps(response),
            content_type="application/json"
        )


def get_docs(post):
    docs = Document.objects.filter(content_type=ContentType.objects.get_for_model(BlogPost).id, object_id=post.id)
    return [(doc, get_doc_type(doc)) for doc in docs]


def get_doc_type(doc):
    ext = doc.file.name.split('.')[-1]
    if ext in ['zip', 'pdf']:
        return ext
    if ext in ['doc', 'docx']:
        return 'doc'
    return 'file'

