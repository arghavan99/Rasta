from django.db import models
from ckeditor.fields import RichTextField


class Event(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    poster = models.ImageField(upload_to='event_posters/', null=True, blank=True) #todo false
    summary = models.TextField(null=False, blank=False)
    description = RichTextField(null=False, blank=False)
    location = models.CharField(max_length=100, null=True, blank=True) #todo false
    date = models.DateField(null=True, blank=True) # todo false

    def __str__(self):
        return self.name


class Document(models.Model):
    caption = models.CharField(max_length=200, null=False, blank=False)
    file = models.FileField(null=False, blank=False, upload_to='event_documents/')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.file.name)


class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/', null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event) + ' - ' + str(self.photo.name)



