from rest_framework.serializers import ModelSerializer
from .models import Player, Team, GameSession

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class GameSessionSerializer(ModelSerializer):
    class Meta:
        model = GameSession
        fields = '__all__'
