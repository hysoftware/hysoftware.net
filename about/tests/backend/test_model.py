'''
About page unit test
'''
# pylint: disable=too-few-public-methods

import hashlib
from django.test import TestCase
from django.core.management import call_command
from ...models import Developer

# pylint: disable=invalid-name
ripemd160 = hashlib.new("ripemd160")
# pylint: enable=invalid-name


class ModelTest(TestCase):
    '''
    Model test
    '''

    developer = None
    TARGET_EMAIL = "admin@hysoftware.net"
    ripemd160.update(TARGET_EMAIL.encode())
    BASIC_INFO = {
        "firstname": "Hiroaki",
        "lastname": "Yamamoto",
        "title": "Main Developer at hysoft",
        "hash": ripemd160.hexdigest()
    }

    def setUp(self):
        '''
        Setup fixture
        '''
        call_command(
            "loaddata",
            "about/fixtures/testdata.json"
        )
        self.basic_data = self.BASIC_INFO.copy()
        # pylint: disable=no-member
        self.developer = Developer.objects.get(
            email=self.TARGET_EMAIL
        )
        # pylint: enable=no-member

    def test_to_dict_basic(self):
        '''
        Calling Developer().to_dict(), returns basic information
        '''

        self.assertDictEqual(self.developer.to_dict(), self.basic_data)

    def test_to_dict_basic_email(self):
        '''
        Calling Developer().to_dict with email=True,
        returns basic information with email
        '''

        email = self.developer.to_dict(email=True).get("email")
        self.assertIsInstance(email, str)

    def test_to_dict_programming(self):
        '''
        Calling Developer().to_dict with programming_langs=True,
        returns basic information with programming languages
        '''
        programming_langs = self.developer.to_dict(
            programming_langs=True
        ).get("programming_languages")
        self.assertIsInstance(programming_langs, list)

        for lang in programming_langs:
            self.assertIsInstance(lang, dict)
            self.assertIsInstance(lang.get("name"), str)

    def test_to_dict_natural(self):
        '''
        Calling Developer().to_dict with natural_langs=True,
        returns basic information with natural languages
        '''
        natural_langs = self.developer.to_dict(
            natural_langs=True
        ).get("natural_languages")
        self.assertIsInstance(natural_langs, list)

        for lang in natural_langs:
            self.assertIsInstance(lang, dict)
            self.assertIsInstance(lang.get("name"), str)

    def test_to_dict_acceptable_vms(self):
        '''
        Calling Developer().to_dict with acceptable_vms=True,
        returns basic information with acceptable vms
        '''
        acceptable_vms = self.developer.to_dict(
            acceptable_vms=True
        )["acceptable_vms"]
        self.assertIsInstance(acceptable_vms, list)

        for acceptable_vm in acceptable_vms:
            self.assertIsInstance(acceptable_vm, dict)
            self.assertIsInstance(acceptable_vm["type"], str)
            self.assertIsInstance(acceptable_vm["type_name"], str)
            self.assertIsInstance(acceptable_vm["name"], str)
            self.assertIsInstance(acceptable_vm["url"], str)

    def test_to_dict_websites(self):
        '''
        Calling Developer().to_dict with websites=True,
        returns basic information with websites
        '''
        websites = self.developer.to_dict(websites=True).get("websites")
        self.assertIsInstance(websites, list)

        for website in websites:
            self.assertIsInstance(website, dict)
            self.assertIsInstance(website["type"], str)
            self.assertIsInstance(website["type_name"], str)
            self.assertIsInstance(website["name"], str)
            self.assertIsInstance(website["url"], str)

    def test_by_hash(self):
        '''
        Calling Developer.by_hash should be matched with basic data
        '''
        hiroaki = Developer.by_hash(self.basic_data["hash"])
        self.assertDictEqual(self.basic_data, hiroaki.to_dict())

    def test_by_hash_non_match(self):
        '''
        Calling Developer.by_hash should be None
        '''
        self.assertIsNone(Developer.by_hash("zxvmnpop"))
