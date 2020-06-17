from django.db import IntegrityError
from django.test import TestCase
from apps.newsletter import views
from apps.newsletter.models import *
import jdatetime


class NewsletterTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        sub1 = Subscriber.objects.create(email='valid.email@email.com')

    def test_duplicate_emails_not_allowed(self):
        try:
            sub1 = Subscriber.objects.create(email='valid.email@email.com')
            self.fail()
        except IntegrityError:
            pass

    def test_subscriber_date(self):
        sub = Subscriber.objects.get(id=1)
        sub_date=sub.date_joint
        self.assertEqual(jdatetime.date.today(), sub_date.date())
        self.assertEqual(jdatetime.datetime.now().hour, sub_date.hour)

    def test_response_successful(self):
        sub = Subscriber.objects.get(id=1)
        response = views.unsubscribe(print(), sub.unique_id)
        self.assertEqual(response.status_code, 200)
        self.assertRaises(Exception, Subscriber.objects.get, unique_id=sub.unique_id)
