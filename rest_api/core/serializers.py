from rest_framework.serializers import ModelSerializer
from .models import Player, Team, GameSession


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['username', 'team']

class TeamSerializer(ModelSerializer):
    players = PlayerSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['name', 'points', 'players', 'id']

class GameSessionSerializer(ModelSerializer):
    team1 = TeamSerializer()
    team2 = TeamSerializer()
    owner = PlayerSerializer()

    class Meta:
        model = GameSession
        fields = ['team1', 'team2', 'id', 'current_round', 'words_per_player', 'owner']
