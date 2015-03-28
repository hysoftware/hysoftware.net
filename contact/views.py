'''
Conctact form views
'''

from django.shortcuts import render
from about.models import Developer


def contact(request, dev_hash=None):
    '''
    Returns contact view
    '''
    # pylint: disable=unused-argument, no-member
    developers = [
        developer.to_dict() for developer in Developer.objects.all()
    ]
    # pylint: enable=no-member

    return render(
        request,
        "contact.html",
        {
            "developers": developers,
            "dev_hash": dev_hash
        }
    )
