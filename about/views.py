'''
from django.shortcuts import render

# Create your views here.
'''

from django.shortcuts import render

from .models import (
    Developer,
    Occupation,
    JobTable,
    ProgrammingLanguage,
    NaturalLanguage,
    Tag,
    ExternalWebsite
)


def about_view(request):
    '''
    About view model.
    Note that this app is using AngularJS for frontend.
    Hence, sandwiching html header/footer is not needed.
    '''
    # pylint: disable=no-member
    developers = Developer.objects.all()
    people = []
    for developer in developers:
        people.append(
            {
                "firstname": developer.first_name,
                "lastname": developer.last_name,
                "programming_languages": [
                    {
                        "name": pg_lang.language
                    } for pg_lang in ProgrammingLanguage.objects.filter(
                        user=developer.email
                    )
                ],
                "natural_languages": [
                    {
                        "name": nt_lang.language
                    } for nt_lang in NaturalLanguage.objects.filter(
                        user=developer.email
                    )
                ],
                "occupations": [
                    {
                        "name": occupation.job_name,
                        "where": occupation.where,
                        "start": occupation.start_year,
                        "end": occupation.end_year or "present",
                        "description": occupation.description
                    } for occupation in Occupation.objects.filter(
                        user=developer.email
                    )
                ],
                "where_to_post_jobs": [
                    {
                        "agent": table.agent,
                        "name": table.name,
                        "url": table.url
                    } for table in JobTable.objects.filter(
                        user=developer.email
                    )
                ],
                "websites": [
                    {
                        "type": website.website_type,
                        "title": website.title,
                        "url": website.url
                    } for website in ExternalWebsite.objects.filter(
                        user=developer.email
                    )
                ],
                "tags": [
                    {
                        "name": tag.name
                    } for tag in Tag.objects.filter(
                        user=developer.email
                    )
                ]
            }
        )
    # pylint: enable=no-member
    render_args = {
        "people": people,
    }
    if len(people) > 1:
        render_args.update(
            {
                "i": "we",
                "I": "We",
                "iam": "we are",
                "Iam": "We are",
                "Ami": "Are we",
                "ami": "are we",
                "my": "our",
                "My": "Our",
                "me": "us"
            }
        )
    else:
        render_args.update(
            {
                "i": "I",
                "I": "I",
                "iam": "I am",
                "Iam": "I am",
                "Ami": "Am I",
                "ami": "am I",
                "my": "my",
                "My": "My",
                "me": "me"
            }
        )
    return render(
        request,
        "about.html",
        render_args
    )
