'''
About page unit test
'''
# pylint: disable=too-few-public-methods

from django.test import TestCase
from django.core.management import call_command
from ...models import Developer


class ModelTest(TestCase):
    '''
    Model test
    '''

    def setUp(self):
        '''
        Setup fixture
        '''
        call_command(
            "loaddata",
            "about/fixtures/hiroaki.json"
        )

    def test_to_dict_basic(self):
        '''
        Calling Developer().to_dict(), returns basic information
        '''
        # pylint: disable=no-member
        developer = Developer.objects.get(
            email="admin@hysoftware.net"
        )

        # pylint: enable=no-member
        self.assertDictEqual(
            developer.to_dict(), {
                "firstname": "Hiroaki",
                "lastname": "Yamamoto",
                "email": "admin@hysoftware.net",
                "title": "Main Developer at hysoft"
            }
        )
