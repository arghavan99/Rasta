import jdatetime
from django.test import TestCase
from django.core.files import File
from PIL import Image
from io import BytesIO

from apps.blog.forms import *
from apps.blog.models import Category, BlogPost , Comment,Reply
from apps.blog import views


class BlogTest(TestCase):
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
                                        summary='summary of first post in blog', text='text of first post in blog')

        post2 = BlogPost.objects.create(title='second post', photo=cls.get_image_file('photo2'),
                                        summary='summary of second post in blog', text='text of second post in blog',
                                        publish_date='1399-1-26')

        post1.categories.add(cat1)
        post1.categories.add(cat3)
        post2.categories.add(cat2)

        comment1 = Comment.objects.create(author_name='ali', text='test text', email='valid.email@gmail.com',
                                         post=post1)
        reply1 = Reply.objects.create(author_name='Sara' , text='test text' ,email='valid.email@gmail.com',comment=comment1)

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
        self.assertEquals(max_length, 70)

    def test_view_url_exists(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_post_categories(self):
        post = BlogPost.objects.get(id=1)
        cat_numbers = post.categories.count()
        self.assertEqual(cat_numbers, 2)

    def test_post_date_is_today(self):
        post = BlogPost.objects.get(id=1)
        post_date = post.publish_date
        self.assertEqual(jdatetime.date.today(), post_date.date())

    def test_not_null_field(self):
        try:
            a = BlogPost.objects.create()
            a.clean_fields()
        except:
            print("BlogPost have some not null fields!")

    def test_cat_url(self):
        response = self.client.get('/blog/sport/')
        self.assertEqual(response.status_code, 200)

    def test_singlePost_url(self):
        response = self.client.get('/blog/posts/1/first post/')
        self.assertEqual(response.status_code, 200)

    def test_singlePost_template(self):
        response = self.client.get('/blog/posts/1/first post/')
        self.assertTemplateUsed(response, 'blog/single_post.html')

    def test_wrong_path_view_uses_correct_template(self):
        response = views.get_single_post(print(), 5, "")
        self.assertEqual(response.status_code, 404)

    # form test
    def test_valid_CommentForm(self):
        post = BlogPost.objects.get(id=1)
        form = CommentForm(data={'author_name': 'Ali',
                                 'email': 'valid.email@gmail.com',
                                 'text': 'Test text',
                                 'post': post.pk})
        self.assertTrue(form.is_valid())

    def test_valid_ReplyForm(self):
        comment = Comment.objects.get(id=1)
        form = ReplyForm(data={'author_name': 'sara',
                                 'email': 'valid.email@gmail.com',
                                 'text': 'Test text',
                                 'is_admin_reply':False,
                                 'comment': comment.pk})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        post = BlogPost.objects.get(id=1)
        form = CommentForm(data={'author_name': 'Ali',
                                 'email': 'invalid.email',
                                 'text': 'Test text',
                                 'post': post.pk})
        self.assertFalse(form.is_valid())

    def test_invalid_form_submission(self):
        post = BlogPost.objects.get(id=1)
        response = self.client.post('/blog/posts/1/first post/', data={'author_name': 'Ali',
                                                                       'email': 'valid.email@gmail.com',
                                                                       'text': 'Test text',
                                                                       'post': post.pk,
                                                                       'is_comment': True,
                                                                       'bibot-response': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/reply_form.html')

    def test_comment_date_is_auto(self):
        comment = Comment.objects.get(id=1)
        comment_date = comment.date_time
        self.assertEqual(jdatetime.date.today(), comment_date.date())
        self.assertEqual(jdatetime.datetime.now().hour ,comment_date.hour)