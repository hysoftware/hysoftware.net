'''
Job models
'''

from django.db import models


class Occupation(models.Model):
    '''
    Occupations
    '''
    # pylint: disable=too-few-public-methods
    job_name = models.CharField(max_length=30, db_index=True)
    where = models.CharField(max_length=100, db_index=True)
    description = models.TextField(default="", db_index=False)
    start_year = models.DateField()
    end_year = models.DateField(null=True, blank=True)
    user = models.ForeignKey("Developer")


class JobTable(models.Model):
    '''
    Job Table
    '''
    # pylint: disable=too-few-public-methods

    AGENTS = (
        ("OD", "oDesk"),
        ("EL", "Elance"),
        ("AS", "Assembly"),
        ("OT", "Other")
    )
    agent = models.CharField(
        max_length=4,
        db_index=True,
        choices=AGENTS
    )
    name = models.CharField(max_length=30, db_index=True)
    url = models.URLField(null=True, blank=True)
    user = models.ForeignKey("Developer")
