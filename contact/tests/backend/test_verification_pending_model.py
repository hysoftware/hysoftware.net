'''
Verification Pending Check
'''

from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.core.management import call_command

from ...models import PendingVerification
from about.models import Developer


class VerificationPendingExpirationTest(TestCase):
    '''
    VerificationPending model pest
    '''

    def setUp(self):
        '''
        Setup
        '''
        call_command("loaddata", "about/fixtures/testdata.json")
        PendingVerification(
            email_hash="85a1661fe0c401f4523caadd1e98b828e8a98fbe",
            token_hash="85a1661fe0c401f4523caadd1e98b828e8a98fbe",
            assignee=Developer(email="admin@hysoftware.net"),
            name="Test example",
            message="Test",
            expires=timezone.now() - timedelta(minutes=2)
        ).save()

    def test_expired_token_removed(self):
        '''
        Expired token should be
        '''
        PendingVerification.remove_expired()
        # pylint: disable = no-member
        self.assertEqual(
            len(PendingVerification.objects.all()),
            0
        )
        # pylint: enable = no-member
