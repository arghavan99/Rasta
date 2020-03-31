from django.shortcuts import render


# Create your views here.
from apps.contact_us.models import *
from apps.contact_us.forms import ContactUsForm


def get_members(request):
    if request.method == 'GET':
        form = ContactUsForm()
        members = RastaMember.objects.all().order_by('id')
        context = {'members': members,
                   'form': form}
        return render(request, 'contact_us/contact_us.html', context)
    else:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        # todo redirect to another page




