'''
Contact form model
'''

from common import gen_hash
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# pylint: disable=too-few-public-methods


class VerifiedEmail(models.Model):
    '''
    Verified email list.
    Note that email field should be RIPEMD160 to prevent leak.
    '''
    email_hash = models.CharField(max_length=40, primary_key=True)
    assignee = models.ForeignKey("about.Developer")

    @classmethod
    def find_by_email(cls, email, assignee=None):
        '''
        Find the instance by email
        '''
        # pylint: disable=no-member
        if assignee:
            return cls.objects.filter(
                email_hash=gen_hash(email),
                assignee=assignee
            )
        else:
            return cls.objects.filter(
                email_hash=gen_hash(email)
            )
        # pylint: enable=no-member

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
    token_hash = models.CharField(
        max_length=40,
        unique=True
    )
    assignee = models.ForeignKey("about.Developer")
    name = models.TextField()
    message = models.TextField(default="")
    expires = models.DateTimeField()

    def set_token(self, token):
        '''
        Set token
        '''
        self.token_hash = gen_hash(token)
        return self

    @classmethod
    def find_by_email(cls, email, assignee=None):
        '''
        Find the instance by email
        '''
        # pylint: disable=no-member
        if assignee:
            return cls.objects.filter(
                email_hash=gen_hash(email),
                assignee=assignee
            )
        else:
            return cls.objects.filter(
                email_hash=gen_hash(email)
            )
        # pylint: enable=no-member

    @classmethod
    def find_by_token(cls, token):
        '''
        Find by token
        '''
        try:
            # pylint: disable=no-member
            return cls.objects.get(gen_hash(token))
            # pylint: enable=no-member
        except ObjectDoesNotExist:
            return None

    @classmethod
    def remove_expired(cls):
        '''
        Remove expired verifications
        '''
        from django.utils import timezone

        # pylint: disable=no-member
        cls.objects.filter(expires__lt=timezone.now()).delete()
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
