import django
from django.db import models
from django.core.mail import EmailMultiAlternatives, EmailMessage, send_mail


# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joint = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.email)


class EmailText(models.Model):
    subject = models.CharField(null=False, blank=False, max_length=100)
    text = models.TextField(null=False, blank=False, max_length=1000)
    link = models.CharField(null=True, blank=True, max_length=400)
    link_text = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.subject

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            super(EmailText, self).save(force_insert, force_update, using, update_fields)
            all_subscribers = list(Subscriber.objects.all())
            for s in all_subscribers:
                send_mail(
                    subject=self.subject,
                    message=self.text,
                    from_email='noreply@rastaeiha.ir',
                    recipient_list=[s.email],
                    fail_silently=False,
                )
