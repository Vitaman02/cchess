from django.urls import path, include
from . import views


app_name="frontend"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<str:name>", views.homepage),
    path("play", views.play, name="play"),
    path("register", views.register, name="register"),
    path("login", views.loginpage, name="login"),
    path("logout", views.logoutpage, name="logout"),
    path("analysis", views.analysis, name="analysis"),
    path("profile/<str:username>", views.homepage, name="profile")
]
