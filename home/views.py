'''
home page view
'''

from django.shortcuts import render

# Create your views here.


def index(request):
    '''
    Returns index page
    '''
    return render(request, "index.html")
