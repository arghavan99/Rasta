from django import forms
from captcha.fields import ReCaptchaField

from apps.contact_us.models import UserFeedback


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'text', 'email', 'type']

    captcha = ReCaptchaField()
