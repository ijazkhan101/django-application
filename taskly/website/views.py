from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('<h1> index page </h1>')
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def student_home(request):
    return HttpResponse("student  page")
