'''
home page view
'''

from django.shortcuts import render
from about.models import Developer

# Create your views here.


LINKS = [
    {
        "name": "About",
        "sref": "about"
    }, {
        "name": "Contact",
        "sref": "contact"
    }
]


def index(request):
    '''
    Returns index page
    '''
    return render(
        request,
        "index.html",
        {"links": LINKS}
    )


def home(request):
    '''
    Returns home page
    '''
    # pylint: disable=no-member
    developers = [
        developer.to_dict(
            programming_langs=True,
            natural_langs=True
        ) for developer in Developer.objects.all()
    ]
    # pylint: enable=no-member
    return render(
        request,
        "home.html",
        {
            "pros": developers,
            "links": LINKS
        }
    )
