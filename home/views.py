'''
home page view
'''

from django.shortcuts import render
from about.models import (
    Developer,
    ProgrammingLanguage,
    NaturalLanguage,
    Occupation
)

# Create your views here.


def index(request):
    '''
    Returns index page
    '''
    # pylint: disable=no-member
    developers = [
        {
            "id": developer.email,
            "first_name": developer.first_name,
            "last_name": developer.last_name
        } for developer in Developer.objects.all()
    ]
    for developer in developers:
        developer["programming_languages"] = [
            language.language
            for language in ProgrammingLanguage.objects.filter(
                user=developer["id"]
            )
        ]
        developer["natural_languages"] = [
            language.language
            for language in NaturalLanguage.objects.filter(
                user=developer["id"]
            )
        ]
        developer["occupations"] = [
            job.job_name
            for job in Occupation.objects.filter(
                user=developer["id"]
            )
        ]
        del developer["id"]

    # pylint: enable=no-member
    return render(
        request,
        "index.html",
        {
            "pros": developers
        }
    )
