from rest_framework import serializers
from .models import Player, Game, Board


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
    

class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"