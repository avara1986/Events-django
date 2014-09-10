"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from events.api.api import EventList, AttendeeList


class landingTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_200(self):
        index_res = self.client.get(reverse('index_landing'))
        self.assertEqual(index_res.status_code, 200)
