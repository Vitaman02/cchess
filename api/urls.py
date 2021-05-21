from django.urls import path
from . import views


app_name = "api"


urlpatterns = [
    # Main Paths
    path("", views.homepage, name="homepage"),

    # API Paths
    path("api/games", views.GameView.as_view(), name="api-games"),
]