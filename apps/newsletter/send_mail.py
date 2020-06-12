from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from apps.newsletter.models import Subscriber


def send_mail_to_subscribers(context, subject):
    all_subscribers = list(Subscriber.objects.all())
    html_message = render_to_string('newsletter/content.html', context)
    plain_message = strip_tags(html_message)
    for s in all_subscribers:
        print('mail is sending to', s.email)
        send_mail(
            subject,
            plain_message,
            'noreply@rastaeiha.ir',
            [s.email],
            html_message=html_message,
            fail_silently=False,
        )