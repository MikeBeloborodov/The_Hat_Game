from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Player, Team, GameSession
from .serializers import PlayerSerializer, TeamSerializer, GameSessionSerializer

@api_view(['GET', 'POST', 'DELETE'])
def player(request, pk=0):
    if request.method == 'POST':
        username = request.data['username']
        try:
            player = Player.objects.get(username=username)
            if player.is_active:
                context = {
                    'error_message': 'Такой игрок уже зашел в игру.'
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                player.is_active = True
                player.save()
                context = {
                    'player_login': 'Добро пожаловать!'
                }
                return Response(context, status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            serializer = PlayerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                context = {
                    'new_player': serializer.data
                }
                return Response(context, status=status.HTTP_201_CREATED)
            else:
                context = {
                    'error_message': serializer.errors
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def player_logout(request):
    username = request.data['username']
    try:
        player = Player.objects.get(username=username)
        player.is_active = False
        player.save()
        context = {
            'logout': 'Игрок вышел'
        }
        return Response(context, status=status.HTTP_200_OK)
    except:
        context = {
            'error_message': 'Такого игрока не существует'
        }
        return Response(context, status=status.HTTP_404_NOT_FOUND)
