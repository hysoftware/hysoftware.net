'''
External Website Models
'''
from django.db import models


class ExternalWebsite(models.Model):
    '''
    External webpages
    '''
    # pylint: disable=too-few-public-methods
    CHOICE = (
        ("G+", "Google Plus"),
        ("LI", "Linkedin"),
        ("FB", "Facebook"),
        ("TW", "Twitter"),
        ("CW", "Coderwalll"),
        ("GH", "Github"),
        ("BB", "Bitbucket"),
        ("OT", "Other")
    )
    choice = models.CharField(
        max_length=4,
        choices=CHOICE,
        db_index=True
    )
    title = models.CharField(
        max_length=30,
        db_index=True,
        null=True,
        blank=True
    )
    url = models.URLField()
    user = models.ForeignKey("Developer")
