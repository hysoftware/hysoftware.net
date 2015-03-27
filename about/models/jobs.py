'''
Job models
'''

from django.db import models


class JobTable(models.Model):
    '''
    Job Table
    '''
    # pylint: disable=too-few-public-methods

    TYPES = (
        ("OD", "oDesk"),
        ("EL", "Elance"),
        ("DR", "Direct Contract")
    )
    website_type = models.CharField(
        max_length=4,
        db_index=True,
        choices=TYPES
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
            self.website_type
        )

    def website_type_name(self):
        '''
        Returns agent name
        '''
        filtered_agents = [
            search for search in self.TYPES if search[0] == self.website_type
        ]
        if len(filtered_agents) != 1:
            raise ValueError(
                (
                    "Awww!! website type {} is invalid!!"
                ).format(self.website_type)
            )
        return filtered_agents[0][1]

    __unicode__ = __str__
