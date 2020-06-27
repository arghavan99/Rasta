from django.core.exceptions import ValidationError

from django.conf import settings
import requests
from django.contrib import messages


def check_bibot_response(request):
    if request.POST.get('bibot-response') is not None:
        if request.POST.get('bibot-response') != '':
            r = requests.post('https://api.bibot.ir/api1/siteverify/', data={
                'secret': settings.bibot_SiteSecretKey,
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


def validate_image_size(image):
    limit_mb = 5
    file_size = image.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

def validate_square_image(image):
    width = image.width
    height = image.height
    temp = height/width
    if temp > 1.1 or temp < 0.9:
        raise ValidationError("This image is not squared")


def validate_file_size(file):
    limit_mb = 10
    file_size = file.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

