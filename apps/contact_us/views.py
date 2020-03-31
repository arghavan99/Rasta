from django.shortcuts import render


# Create your views here.

def get_members(request):
    return render(request, 'contact_us/contact_us.html')
