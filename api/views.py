from django.shortcuts import render

from rest_framework import generics

from .models import Game
from api.serializers import GameSerializer


def homepage(request):
    return render(request, "api/index.html")


class GameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer