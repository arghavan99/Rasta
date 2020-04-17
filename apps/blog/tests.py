import jdatetime
from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO
from apps.blog.models import Category, BlogPost


class CategoryTest(TestCase):
    @staticmethod
    def get_image_file(name, ext='png', size=(300, 400), color=(255, 0, 0)):
        file_obj = BytesIO()
        image = Image.new('RGBA', size=size, color=color)
        image.save(file_obj, format=ext, quality=100)
        file_obj.seek(0)
        return File(file_obj, name=name)

    @classmethod
    def setUpTestData(cls):
        cat1 = Category.objects.create(title='education', url='education')
        cat2 = Category.objects.create(title='sport', url='sport')
        cat3 = Category.objects.create(title='politics', url='politics')

        post1 = BlogPost.objects.create(title='first post', photo=cls.get_image_file('photo1'),
                                        summary='summary of first post in blog', text='text of first post in blog',
                                        publish_date='1399-1-26')

        post2 = BlogPost.objects.create(title='second post', photo=cls.get_image_file('photo2'),
                                        summary='summary of second post in blog', text='text of second post in blog',
                                        publish_date='1399-1-26')

        post1.categories.add(cat1)
        post1.categories.add(cat3)

        post2.categories.add(cat2)

    def test_title_max_length(self):
        cat = Category.objects.get(id=1)
        max_length = cat._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_url_max_length(self):
        cat = Category.objects.get(id=1)
        max_length = cat._meta.get_field('url').max_length
        self.assertEquals(max_length, 20)

    def test_title_blog_max_length(self):
        post = BlogPost.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_view_url_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_categories(self):
        post = BlogPost.objects.get(id=1)
        cat_numbers = post.categories.count()
        self.assertEqual(cat_numbers, 2)

    def test_post_date_before_today(self):
        post = BlogPost.objects.get(id=1)
        post_date = post.publish_date
        self.assertGreater(jdatetime.date.today(),post_date.date())

    def test_not_null_field(self):
        try:
            a = BlogPost.objects.create()
            a.clean_fields()
        except:
            print("BlogPost have some not null fields!")

    def test_cat_url(self):
        response = self.client.get('/blog/sport/')
        self.assertEqual(response.status_code, 200)




