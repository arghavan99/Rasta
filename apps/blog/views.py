from django.shortcuts import render
from apps.blog.models import *


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
        'publish_date': post.publish_date,
        'summary': post.summary,
        'categories': [cat_dictionary(cat) for cat in post.categories.all()]
    }


def vis_hid_cats(num, categories):
    if len(categories) < num:
        hid_cats = []
        vis_cats = categories
    else:
        vis_cats = categories[:num]
        hid_cats = categories[num:]
    context = {
        'vis_cats': [cat_dictionary(cat) for cat in vis_cats],
        'hid_cats': [cat_dictionary(cat) for cat in hid_cats]
    }
    return context


def get_all_posts(request):
    categories = Category.objects.all()
    posts = BlogPost.objects.order_by('publish_date')
    context = vis_hid_cats(8, categories)
    context['active_cat'] = ''
    context['posts'] = [post_dictionary(post) for post in posts]
    print(context)
    return render(request, 'blog/blog.html', context)


def get_posts(request, cat_url):
    active_cat = Category.objects.filter(url=cat_url)[0]
    # todo 404 if active_cat does not exist
    categories = Category.objects.exclude(id=active_cat.id)
    context = vis_hid_cats(7, categories)
    context['active_cat'] = cat_dictionary(active_cat)
    posts = BlogPost.objects.order_by('publish_date').filter(categories__in=[active_cat])
    # todo eyes 1 , 2, 3
    context['posts'] = [post_dictionary(post) for post in posts]
    print(context)
    return render(request, 'blog/blog.html', context)
