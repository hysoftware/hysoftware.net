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

    def __str__(self):
        '''
        Represents the class
        '''
        return (
            "User tag of {}: {}"
        ).format(self.user, self.tag_name)
