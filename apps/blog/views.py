from django.shortcuts import render
from apps.blog.models import *


def get_posts(request):
    categories = Category.objects.all()
    context = {'categories': list(categories)}
    if request.method == 'GET':
        posts = BlogPost.objects.all().order_by('publish_date')
    else:
        cat_id = request['category']
        cat = Category.objects.filter(id=cat_id)[0]
        # todo 404 if cat_id does not exist
        posts = BlogPost.objects.filter(categories__in=[cat])
    # todo eyes 1 , 2, 3
    context['posts'] = [
        {
            'id': post.id,
            'title': post.title,
            'photo': post.photo,
            'publish_date': post.publish_date,
            'summary': post.summary,
            'categories': [
                {
                    'id': cat.id,
                    'title': cat.title
                } for cat in post.categories.all()
            ]
        } for post in posts]
    return render(request, 'blog/blog.html', context)
