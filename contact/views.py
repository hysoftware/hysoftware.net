'''
Conctact form views
'''

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from about.models import Developer

from .models import VerifiedEmail


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


def check_email_in_list(request, dev_hash):
    '''
    Checks whether requested email is in developer's list
    '''
    developer = Developer.by_hash(dev_hash)

    if not developer:
        # We don't know such developer!
        return HttpResponse(status=404)

    # Check developer's list
    his_list = None
    try:
        his_list = VerifiedEmail.find_by_email(
            request.GET["sender"],
            developer.email
        )
    except MultiValueDictKeyError:
        # This error is only thrown when sender is null.
        return HttpResponse(status=404)

    if his_list and len(his_list) > 0:
        # He is listed on developer's list
        return HttpResponse(status=200)
    return HttpResponse(status=404)
