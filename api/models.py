from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bullet_elo = models.IntegerField(default=1200)
    blitz_elo = models.IntegerField(default=1200)
    rapid_elo = models.IntegerField(default=1200)
    classical_elo = models.IntegerField(default=1200)

    joined_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_games(self):
        return self.game_set.all().order_by("-id")

    def __str__(self):
        return self.user.username



# Create get 2D positions method
class Game(models.Model):
    class OutcomeChoices(models.TextChoices):
        WHITE = ("WH", "WHITE")
        BLACK = ("BL", "BLACK")
        DRAW = ("DR", "DRAW")
    player_white = models.ForeignKey(Player, related_name="white", on_delete=models.DO_NOTHING)
    player_black = models.ForeignKey(Player, related_name="black", on_delete=models.DO_NOTHING)
    winner = models.CharField(max_length=2, choices=OutcomeChoices.choices)
    dated = models.DateTimeField(auto_now_add=True)

    @property
    def number_of_moves(self):
        moves = self.board_set.last().move_number 
        return  moves // 2 + moves % 2

    def __str__(self):
        return f"{self.dated} {self.player_white} vs {self.player_black}"


class Board(models.Model):
    """The board at each position of the game

    chess games count moves after each player has played once,
    but in this case we increment by one after each player's move
    and handle it in the Game model
    """
    move_number = models.IntegerField(default=1)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    position = models.CharField(max_length=10000, default="")