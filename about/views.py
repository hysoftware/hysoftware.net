'''
from django.shortcuts import render

# Create your views here.
'''

from django.shortcuts import render

from .models import (
    Developer,
    JobTable,
    ProgrammingLanguage,
    NaturalLanguage,
    Tag,
    ExternalWebsite
)
from .noum_generator import generate_first_person


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
                "title": developer.title,
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
                "acceptable_vms": [
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
    render_args.update(generate_first_person(people))
    return render(
        request,
        "about.html",
        render_args
    )
