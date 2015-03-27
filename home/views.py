'''
home page view
'''

from django.shortcuts import render
from about.models import (
    Developer
)

# Create your views here.


def index(request):
    '''
    Returns index page
    '''
    # pylint: disable=no-member
    developers = [
        developer.to_dict(
            programming_langs=True,
            natural_langs=True
        ) for developer in Developer.objects.all()
    ]

    # pylint: enable=no-member
    links = [
        {
            "name": "About",
            "sref": "about"
        }
    ]
    return render(
        request,
        "index.html",
        {
            "pros": developers,
            "links": links
        }
    )
