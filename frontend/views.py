from django.http.response import HttpResponse
from django.shortcuts import render


def homepage(request, *args, **kwargs):
    return render(request, "frontend/index.html")


# ---- REGISTER -----
def register(request):
    return render(request, "frontend/register.html")


# ---- LOGIN ------
def loginpage(request):
    return render(request, "frontend/login.html")


def logoutpage(request):
    return HttpResponse("logout")


# ----- PROFILE ------
def profile(request, username):
    print(username)
    return render(request, "frontend/profile.html")


# ----- PLAY -----
def play(request):
    return render(request, "frontend/play.html")


# ----- ANALYSIS -----
def analysis(request):
    return render(request, "frontend/analysis.html")


def test(request, name):
    return HttpResponse("Hi")