from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.contact_us.models import RastaMember
from apps.contact_us.forms import ContactUsForm


class RastaMemberTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        RastaMember.objects.create(name='Shadi Ghasemi', education='Computer Engineering Student', role='Member',
                                   photo_visible=cls.get_image_file(name='sh_visible', size=(200, 100)),
                                   photo_hidden=cls.get_image_file(name='sh_hidden', size=(300, 500)))

        RastaMember.objects.create(name='Sara Sadeghi', education='Industrial Engineering Student', role='Manager',
                                   photo_visible=cls.get_image_file(name='s_visible', size=(150, 200)),
                                   photo_hidden=cls.get_image_file(name='s_hidden', size=(340, 150)))

    def test_name_max_length(self):
        member = RastaMember.objects.get(name='Shadi Ghasemi')
        max_length = member._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_education_max_length(self):
        member = RastaMember.objects.get(name='Sara Sadeghi')
        max_length = member._meta.get_field('education').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        member = RastaMember.objects.get(name='Shadi Ghasemi')
        expected_object_name = '%s - %s' % (member.name, member.role)
        self.assertEquals(expected_object_name, str(member))

    def test_photo_visible_resize(self):
        member = RastaMember.objects.get(name='Shadi Ghasemi')
        vis_size = Image.open(member.photo_visible).size
        self.assertEqual((150, 150), vis_size)

    def test_photo_hidden_resize(self):
        member = RastaMember.objects.get(name='Sara Sadeghi')
        hid_size = Image.open(member.photo_visible).size
        self.assertEqual((150, 150), hid_size)


class ContactUsFormTest(TestCase):

    def test_valid_form(self):
        form = ContactUsForm(data={'name': 'Shadi',
                                   'text': 'Form Test',
                                   'email': 'valid.email@gmail.com',
                                   'type': 'student'})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form = ContactUsForm(data={'name': 'Shadi',
                                   'text': 'Form Test',
                                   'email': 'Invalid Email',
                                   'type': 'student'})
        self.assertFalse(form.is_valid())

    def test_invalid_type(self):
        form = ContactUsForm(data={'name': 'Shadi',
                                   'text': 'Form Test',
                                   'email': 'valid.email@gmail.com',
                                   'type': ''})
        self.assertFalse(form.is_valid())


class ContactUsViewTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(50, 50), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        for i in range(6):
            RastaMember.objects.create(name='Member %d' % i, education='Computer Engineering Student', role='Member',
                                       photo_visible=cls.get_image_file(name='photo_vis', size=(100, 100)),
                                       photo_hidden=cls.get_image_file(name='photo_hid', size=(200, 100)))

    def test_view_url_exists(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')

    def test_lists_all_members(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['members']), 6)

    def test_form_exists(self):
        response = self.client.get('/contact_us/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['form'])

    def test_invalid_form_submission(self):
        response = self.client.post('/contact_us/', data={'name': 'Shadi',
                                                          'text': 'Form Test',
                                                          'email': 'valid.email@gmail.com',
                                                          'type': 'student',
                                                          'bibot-response': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_us/contact_us.html')
