# Create your views here.
from courses.models import Courses
from django.shortcuts import render


def home_view(request):
    object_list = Courses.objects.filter()
    return render(request, 'home.html', {
        'object_list': object_list,
        'nav': 'home'
    })


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })
