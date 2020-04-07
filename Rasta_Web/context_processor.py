def menu(request):
    context = {
        'navbar': [
            ['صفحه اصلی', '/'],
            ['رویدادها', '/events'],
            ['بلاگ', '/blog'],
            ['تماس با ما', '/contact_us']
        ]
    }

    path = '/' + request.path.split('/')[1]
    for item in context['navbar']:
        if item[1] == path:
            item.append('active')
        else:
            item.append('')
    return context
