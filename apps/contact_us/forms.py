from django import forms

from apps.contact_us.models import UserFeedback


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['name', 'text', 'email', 'type']
