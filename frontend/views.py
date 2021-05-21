from django.shortcuts import render


def homepage(request, *args, **kwargs):
    return render(request, "frontend/index.html")
