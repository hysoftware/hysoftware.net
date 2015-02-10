'''
Contact form model
'''

# pylint: disable=too-few-public-methods

from django.db import models


class VerifiedEmails(models.Model):
    '''
    Verified email list.
    Note that email field should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(max_length=40, primary_key=True)


class PendingVerification(models.Model):
    '''
    Email verification pending.
    Note that email and token fields should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(max_length=40, primary_key=True)
    token = models.CharField(max_length=40)
    message = models.TextField(default="")
    expires = models.DateTimeField()
