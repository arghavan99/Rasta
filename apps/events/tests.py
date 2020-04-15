from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.events.models import Event

class EventModelTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(300, 400), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        Event.objects.create(name='first event', poster=cls.get_image_file(name='sh_visible', size=(200, 100)),
                             summary='a brief description to tell the story n1',
                             description='a detailed story of event so that everyone get it correctly number one',
                             location='Tehran', date='2020-4-21')

        Event.objects.create(name='second event', poster=cls.get_image_file('poster2'),
                             summary='a brief description to tell the story n2',
                             description='a detailed story of event so that everyone get it correctly number two',
                             location='Iran', date='2000-1-1')
        Event.objects.create(name='third event', poster=cls.get_image_file('poster3'),
                             summary='a brief description to tell the story n3',
                             description='a detailed story of event so that everyone get it correctly number three',
                             location='Yazd', date='2020-2-20')

    def test_title_max_length(self):
        event = Event.objects.get(id=1)
        max_length = event._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)





