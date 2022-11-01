from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

class Player(models.Model):
    username = models.CharField(max_length=100, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

class GameSession(models.Model):
    team1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team1")
    team2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team2")
    players = models.ManyToManyField(Player)

