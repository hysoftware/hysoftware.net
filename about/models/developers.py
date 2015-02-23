'''
Developer profiles
'''

from django.db import models


class Developer(models.Model):
    '''
    Developer Information
    '''
    # pylint: disable=too-few-public-methods
    first_name = models.CharField(max_length=20, db_index=True)
    last_name = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(max_length=40, primary_key=True)
    xero_key = models.CharField(max_length=40, blank=True)
    xero_secret = models.TextField(default="", blank=True)
