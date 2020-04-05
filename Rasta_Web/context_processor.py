from django.urls import reverse
from django.utils.translation import ugettext as _


def menu(request):
    context = {
            'navbar': [
                ['صفحه اصلی', '/'],
                ['رویدادها', 'events/'],
                ['بلاگ', 'blog/'],
                ['تماس با ما', 'contact_us/']
            ]
    }

    for item in context['navbar']:
        if item[1] == request.path:
            item.append('active')
        else:
            item.append('')
    return context