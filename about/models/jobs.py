'''
Job models
'''

from django.db import models


class JobTable(models.Model):
    '''
    Job Table
    '''
    # pylint: disable=too-few-public-methods

    AGENTS = (
        ("OD", "oDesk"),
        ("EL", "Elance"),
        ("DR", "Direct Contract")
    )
    agent = models.CharField(
        max_length=4,
        db_index=True,
        choices=AGENTS
    )
    name = models.CharField(max_length=30, db_index=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey("Developer")

    def __str__(self):
        '''
        Represent the class
        '''
        return (
            "Job table of {}: {} named {} at {}"
        ).format(
            self.user,
            self.url,
            self.name,
            self.agent
        )

    __unicode__ = __str__
