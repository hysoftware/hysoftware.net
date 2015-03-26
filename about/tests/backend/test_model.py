'''
About page unit test
'''

from unittest import skip
from django.test import TestCase
from ...models import Developer


class ModelTest(TestCase):
    '''
    Model test
    '''

    @skip("Not completed yet")
    def test_to_dict_basic(self):
        '''
        Calling Developer().to_dict(), returns basic information
        '''
        # pylint: disable=no-member
        print(Developer.objects.all())
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
