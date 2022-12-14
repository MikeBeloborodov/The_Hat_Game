from django.db import models
from django.utils.translation import gettext_lazy as _

class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    players = models.ManyToManyField('Player', related_name='team_players')

class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    game_session = models.ForeignKey('GameSession', on_delete=models.CASCADE, null=True)

class GameSession(models.Model):
    class Round(models.TextChoices):
        PRE_GAME = 'PG', _('Pre game')
        ROUND_1 = 'R1', _('Round 1')
        ROUND_2 = 'R2', _('Round 2')
        ROUND_3 = 'R3', _('Round 3')

    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="session_owner")
    team1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team2")
    current_round = models.CharField(
        max_length=2,
        choices=Round.choices,
        default=Round.PRE_GAME
    )
    words_per_player = models.IntegerField(default=0)

class Word(models.Model):
    class WordStatus(models.TextChoices):
        GUESSED = 'G', _('Guessed word')
        NOT_GUESSED = 'NG', _('Not guessed word')

    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="word_owner")
    body = models.CharField(max_length=500)
    status = models.CharField(
        max_length=2,
        choices=WordStatus.choices,
        default=WordStatus.NOT_GUESSED
    )
