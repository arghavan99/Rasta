import mimetypes
import os

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import ValidationError
from Rasta_Web.settings import bibot_SiteSecretKey
import requests
from django.contrib import messages


def doc_downloader(request):
    if request.GET:
        original_filename = request.GET['file']
    elif request.POST:
        original_filename = request.POST['original_file_name']
    try:
        x = os.path.abspath(os.path.join(settings.MEDIA_ROOT, original_filename))
        fp = open(x, 'rb')
        response = HttpResponse(fp.read())
        fp.close()
    except:
        return HttpResponseNotFound("فایل درخواست شده یافت نشد!")
    type, encoding = mimetypes.guess_type(x)
    if type is None:
        type = 'application/octet-stream'
    response['Content-Type'] = type
    response['Content-Length'] = str(os.stat(x).st_size)
    if encoding is not None:
        response['Content-Encoding'] = encoding

    original_filename = original_filename.split('/')[-1]
    # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
    if u'WebKit' in request.META['HTTP_USER_AGENT']:
        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
        filename_header = 'filename=%s' % original_filename
    elif u'MSIE' in request.META['HTTP_USER_AGENT']:
        # IE does not support internationalized filename at all.
        # It can only recognize internationalized URL, so we do the trick via routing rules.
        filename_header = ''
    else:
        # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
        filename_header = 'filename*=%s' % original_filename
    response['Content-Disposition'] = 'attachment; ' + filename_header
    return response


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
