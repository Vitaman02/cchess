from django.shortcuts import render

from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Game
from api.serializers import CreateGameSerializer, GameSerializer


def homepage(request):
    return render(request, "api/index.html")


class GameView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class CreateGameView(APIView):
    serializer_class = CreateGameSerializer

    def post(self, request, format=None):
        pass