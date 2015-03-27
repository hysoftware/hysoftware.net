'''
Developer profiles
'''

from django.db import models
from common import gen_hash
from .languages import (
    ProgrammingLanguage,
    NaturalLanguage
)
from .jobs import (
    JobTable
)
from .websites import (
    ExternalWebsite
)


class Developer(models.Model):
    '''
    Developer Information
    '''
    # pylint: disable=too-few-public-methods
    first_name = models.CharField(max_length=20, db_index=True)
    last_name = models.CharField(max_length=20, db_index=True)
    email = models.EmailField(max_length=40, primary_key=True)
    title = models.CharField(max_length=40, db_index=True)

    def to_dict(self, **kwargs):
        '''
        Convert to dict
        '''
        optional = {
            "email": False,
            "programming_langs": False,
            "natural_langs": False,
            "acceptable_vms": False,
            "websites": False
        }
        optional.update(kwargs)

        result = {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "title": self.title,
            "hash": gen_hash(self.email)
        }

        # pylint: disable=no-member
        def __language__(language_class, name, visible):
            if visible:
                result[name] = [
                    {
                        "name": lang.language
                    } for lang in language_class.objects.filter(
                        user=self.email
                    )
                ]

        def __website__(website_class, name, visible):
            if visible:
                result[name] = [
                    {
                        "type": website.website_type,
                        "type_name": website.website_type_name(),
                        "name": website.name,
                        "url": website.url
                    } for website in website_class.objects.filter(
                        user=self.email
                    )
                ]
        # pylint: enable=no-member

        if optional["email"]:
            result["email"] = self.email

        __language__(
            ProgrammingLanguage,
            "programming_languages",
            optional["programming_langs"]
        )
        __language__(
            NaturalLanguage,
            "natural_languages",
            optional["natural_langs"]
        )

        __website__(
            JobTable,
            "acceptable_vms",
            optional["acceptable_vms"]
        )
        __website__(
            ExternalWebsite,
            "websites",
            optional["websites"]
        )

        return result

    @classmethod
    def by_hash(cls, rmd160_hash):
        '''
        Search Develoeprs by hash
        '''
        # pylint: disable=no-member
        developers = [
            developer for developer in cls.objects.all()
            if gen_hash(developer.email) == rmd160_hash
        ]
        # pylint: enable=no-member
        if len(developers) < 1:
            return None
        return developers[0]

    def __str__(self):
        '''
        Represents class
        '''
        return (
            "Developer: {} {} <{}> -- {}"
        ).format(
            self.first_name,
            self.last_name,
            self.email,
            self.title
        )

    __unicode__ = __str__
