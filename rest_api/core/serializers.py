from rest_framework.serializers import ModelSerializer
from .models import Player, Team, GameSession

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'points']

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['username']

class GameSessionSerializer(ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    owner = PlayerSerializer()

    class Meta:
        model = GameSession
        fields = ['team1', 'team2', 'id', 'current_round', 'words_per_player', 'owner']
