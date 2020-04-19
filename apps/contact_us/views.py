from Rasta_Web.settings import bibot_SiteKey, bibot_SiteSecretKey
from apps.contact_us.models import *
from apps.contact_us.forms import ContactUsForm

import requests
from django.contrib import messages
from django.shortcuts import render


def check_bibot_response(request):

    if request.POST.get('bibot-response') is not None:
        if request.POST.get('bibot-response') != '':
            r = requests.post('https://api.bibot.ir/api1/siteverify/', data={
                'secret': bibot_SiteSecretKey,
                'response': request.POST['bibot-response']
            })
            print(r.json())
            if r.json()['success']:
                messages.success(request, 'فرایند تایید هویت شما با موفقیت انجام شد!')
                return True
            elif r.json()['error-codes']:
                for error_code in r.json()['error-codes']:
                    messages.error(request, error_code)
                return False
            else:
                messages.error(request, 'بی‌بات به درستی حل نشده است!')
                return False
        else:
            messages.error(request, 'بی‌بات به درستی حل نشده است!')
            return False
    messages.error(request, 'ارتباط با سرور بی‌بات برقرار نشده است! آیا جاوااسکریپت شما فعال است؟')
    return False


def get_members(request):
    form = ContactUsForm()
    members = RastaMember.objects.all().order_by('id')
    context = {'members': members,
               'form': form,
               'bibot': bibot_SiteKey}
    if request.method == 'GET':
        return render(request, 'base/404.html', context)
    else:
        if not check_bibot_response(request):
            return render(request, 'contact_us/contact_us.html', context)
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact_us/successful.html')
