from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.intro.models import HomepageData, UpcomingEvent


class UpcomingEventTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        UpcomingEvent.objects.create(poster=cls.get_image_file('poster1'), intro='Visible Intro', title='VISIBLE EVENT',
                                     button_link='google.com', button_name='Visit Now', show_on_homepage=True)
        UpcomingEvent.objects.create(poster=cls.get_image_file('poster2'), intro='Hidden Intro', title='HIDDEN EVENT',
                                     button_link='bing.com', button_name='Visit Now', show_on_homepage=False)

    def test_title_max_length(self):
        member = UpcomingEvent.objects.get(title='VISIBLE EVENT')
        max_length = member._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_button_name_max_length(self):
        member = UpcomingEvent.objects.get(show_on_homepage=False)
        max_length = member._meta.get_field('button_name').max_length
        self.assertEquals(max_length, 50)


class IntroViewTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        HomepageData.objects.create(intro='Test Intro', video_url='https://www.aparat.com/v/G0aoc')
        UpcomingEvent.objects.create(poster=cls.get_image_file('poster1'), intro='Visible Intro', title='VISIBLE EVENT',
                                     button_link='google.com', button_name='Visit Now', show_on_homepage=True)
        UpcomingEvent.objects.create(poster=cls.get_image_file('poster2'), intro='Visible Intro', title='LAST EVENT',
                                     button_link='google.com', button_name='Visit Now', show_on_homepage=True)
        UpcomingEvent.objects.create(poster=cls.get_image_file('poster3'), intro='Hidden Intro', title='HIDDEN EVENT',
                                     button_link='bing.com', button_name='Visit Now', show_on_homepage=False)

    def test_view_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'intro/index.html')

    def test_upcoming_event_is_the_last(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['upcoming_event'].title, 'LAST EVENT')

    def test_video_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['aparat_url'],
                         'https://www.aparat.com/video/video/embed/videohash/G0aoc/vt/frame')
