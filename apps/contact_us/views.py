from django.shortcuts import render


# Create your views here.
from apps.contact_us.models import RastaMember


def get_members(request):
    context = {}
    if request.method == 'GET':
        members = RastaMember.objects.all().order_by('id')
        context = {'members': members}
    return render(request, 'contact_us/contact_us.html', context)

