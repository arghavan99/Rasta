from django.core.exceptions import ValidationError

from Rasta_Web.settings import base
import requests
from django.contrib import messages


def check_bibot_response(request):
    if request.POST.get('bibot-response') is not None:
        if request.POST.get('bibot-response') != '':
            r = requests.post('https://api.bibot.ir/api1/siteverify/', data={
                'secret': base.bibot_SiteSecretKey,
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
    if temp > 1.2 or temp < 0.8:
        raise ValidationError("تصویر شما مربعی نیست! برای نمایش بهتر در سایت، بهتر است نسبت ابعاد تصویر بین ۰.۸ تا ۱.۲ باشد. لطفا این نسبت را رعایت کرده و تصویر را مجددا آپلود کنید.")


def validate_file_size(file):
    limit_mb = 30
    file_size = file.file.size
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)

