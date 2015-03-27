'''
Conctact form views
'''

from django.shortcuts import render
from about.models import Developer


def contact(request, developer_hash=None):
    '''
    Returns contact view
    '''

    # pylint: disable=no-member
    developers = [
        developer.to_dict()
        for developer in Developer.objects.all()
    ]
    # pylint: enable=no-member

    return render(
        request,
        "contact.html",
        {
            "developers": developers,
            "selected_hash": developer_hash
        }
    )
