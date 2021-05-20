from django.http.request import HttpRequest
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpRequest("Hi")