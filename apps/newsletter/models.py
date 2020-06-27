import django
from django.db import models
import uuid

# Create your models here.
from django.utils.html import strip_tags


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_joint = models.DateTimeField(default=django.utils.timezone.now)
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

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
            from apps.newsletter.tasks import send_mail_to_subscribers_task
            super(EmailText, self).save(force_insert, force_update, using, update_fields)
            context = {
                'text': self.text,
                'link': self.link,
                'link_text': self.link_text,
            }
            send_mail_to_subscribers_task.delay(context, self.subject)