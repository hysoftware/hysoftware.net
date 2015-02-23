'''
Language Related models
'''

from django.db import models


class ProgrammingLanguage(models.Model):
    '''
    Programming Lnaguages
    '''
    # pylint: disable=too-few-public-methods
    language = models.CharField(max_length=40, db_index=True)
    user = models.ForeignKey("Developer")


class NaturalLanguage(models.Model):
    '''
    Natual Lnaguages
    '''
    # pylint: disable=too-few-public-methods
    language = models.CharField(max_length=40, db_index=True)
    user = models.ForeignKey("Developer")
