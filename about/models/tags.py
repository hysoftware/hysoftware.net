'''
Tags model
'''

from django.db import models


class Tag(models.Model):
    '''
    User tags
    '''
    # pylint: disable=too-few-public-methods
    tag_name = models.CharField(max_length=20, db_index=True)
    user = models.ForeignKey("Developer")
