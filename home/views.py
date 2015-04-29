'''
home page view
'''

from django.shortcuts import render
from about.models import Developer

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
        }, {
            "name": "Github",
            "href": "https://github.com/hysoftware/hysoftware.net"
        }, {
            "name": "Contact",
            "sref": "contact"
        }
    ]
    return render(
        request,
        "index.html",
        {
            "links": links,
            "pros": developers,
            "home_snapshot": request.META.get(
                'REMOTE_HOST', request.META.get("REMOTE_ADDR", "UNKNOWN")
            ).endswith(
                "googlebot.com"
            )
        }
    )
