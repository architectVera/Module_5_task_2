from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
import json


# Create your views here.


def user_register(request: HttpRequest):
    return render(request, 'user_register.html')


def user_login(request: HttpRequest):
    return render(request, 'user_login.html')

