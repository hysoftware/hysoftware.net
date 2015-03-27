'''
Contact form model
'''

from common import gen_hash
from django.db import models

# pylint: disable=too-few-public-methods


class VerifiedEmails(models.Model):
    '''
    Verified email list.
    Note that email field should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(max_length=40, primary_key=True)
    assignee = models.ForeignKey("about.Developer")

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "Verified Email: {} (hash), Asignee: {}"
        ).format(self.email_hash, self.assignee)

    __unicode__ = __str__


class PendingVerification(models.Model):
    '''
    Email verification pending.
    Note that email and token fields should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(
        max_length=40,
        primary_key=True
    )
    assignee = models.ForeignKey("about.Developer")
    message = models.TextField(default="")
    expires = models.DateTimeField()

    @classmethod
    def by_email(cls, email):
        '''
        Return verification pending object by email
        '''
        # pylint: disable=no-member
        return cls.objects.get(email_hash=gen_hash(email))
        # pylint: enable=no-member

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "Email Verification: {} (hash), "
            "Expires: {}, Assignee: {}, "
            "Message: \n {}"
        ).format(
            self.email_hash,
            self.expires,
            self.assignee,
            self.message
        )

    __unicode__ = __str__
