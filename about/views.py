'''
from django.shortcuts import render

# Create your views here.
'''

from django.shortcuts import render

from .models import Developer
from .noum_generator import generate_first_person


def about_view(request):
    '''
    About view model.
    Note that this app is using AngularJS for frontend.
    Hence, sandwiching html header/footer is not needed.
    '''
    # pylint: disable=no-member
    developers = Developer.objects.all()
    people = [
        developer.to_dict(
            programming_langs=True,
            natural_langs=True,
            acceptable_vms=True,
            websites=True
        ) for developer in developers
    ]
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
