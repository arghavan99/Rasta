from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from Rasta_Web.utils import validate_file_size


class Document(models.Model):
    caption = models.CharField(max_length=200, null=False, blank=False)
    file = models.FileField(null=False, blank=False, upload_to='documents/', validators=[validate_file_size])

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={"model__in": ('BlogPost', 'Event')})
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return str(self.content_object) + ' - ' + str(self.file.name)
