'''
Contact form tests.
'''

from django.test import TestCase
from django.core.management import call_command
from common import gen_hash
from .models import VerifiedEmail


class VerifiedEmailTests(TestCase):
    '''
    Verified Email tests
    '''

    def setUp(self):
        '''
        Setup
        '''
        call_command(
            "loaddata",
            "about/fixtures/testdata.json",
            "contact/fixtures/verified_email_testdata.json"
        )

    def test_find_by_email_match(self):
        '''
        Should return matched verification
        '''
        email = VerifiedEmail.find_by_email(
            "test@example.com",
            "admin@hysoftware.net"
        )
        self.assertEqual(len(email), 1)
        self.assertEqual(email[0].email_hash, gen_hash("test@example.com"))

    def test_find_by_email_miss_dev(self):
        '''
        Should return empty list because dev mail
        is different
        '''
        email = VerifiedEmail.find_by_email(
            "test@example.com",
            "test@example.com"
        )
        self.assertEqual(len(email), 0)

    def test_find_by_email_miss_sender(self):
        '''
        Should return empty list because sender mail
        is different
        '''
        email = VerifiedEmail.find_by_email(
            "notmatch@example.com",
            "admin@hysoftware.net"
        )
        self.assertEqual(len(email), 0)
