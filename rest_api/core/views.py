from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Player, Team, GameSession
from .serializers import PlayerSerializer, TeamSerializer, GameSessionSerializer

@api_view(['GET', 'POST', 'DELETE'])
def player(request, pk=0):
    
    if request.method == 'GET':
        username = request.GET.get('q')
        try:
            player = Player.objects.get(username=username)
            serializer = PlayerSerializer(player)
            context = {
                'player': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            context = {
                'error_message': 'Такого игрока не существует.'
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)

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

@api_view(['GET', 'POST', 'DELETE'])
def game_session(request, pk=0):

    if request.method == 'GET':
        if pk == 0:
            sessions = GameSession.objects.all()
            serializer = GameSessionSerializer(sessions, many=True)
            context = {
                'game_sessions': serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            try:
                session = GameSession.objects.get(id=pk)
                serializer = GameSessionSerializer(session)
                context = {
                    'game_session': serializer.data
                }
                return Response(context, status=status.HTTP_200_OK)
            except GameSession.DoesNotExist:
                context = {
                    'error_message': "Такой игры не существует."
                }
                return Response(context, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        team1_name = request.data['team1']
        try:
            team1 = Team.objects.get(name=team1_name)
        except Team.DoesNotExist:
            team1 = Team.objects.create(
                name=team1_name
            )
        team2_name = request.data['team2']
        try:
            team2 = Team.objects.get(name=team2_name)
        except Team.DoesNotExist:
            team2 = Team.objects.create(
                name=team2_name
            )
        username = request.data['username']
        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            context = {
                'error_message': "Такой игрок не существует."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            words_per_player = int(request.data['words_per_player'])
        except Exception:
            context = {
                "error_message": "Укажите правильноe кол-во слов."
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        try:
            session = GameSession.objects.create(
                team1=team1,
                team2=team2,
                owner=player,
                words_per_player=words_per_player
            )
            serializer = GameSessionSerializer(session)
            context = {
                "new_session": serializer.data
            }
            return Response(context, status=status.HTTP_201_CREATED)
        except Exception as e:
            context = {
                "error_message": "Ошибка при создании игры. ",
                "exception": str(e)
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        session_id = request.data['id']
        try:
            session = GameSession.objects.get(id=session_id)
            serializer = GameSessionSerializer(session)
            session.delete()
            context = {
                'deleted_session': serializer.data
            }
            return Response(context, status=status.HTTP_204_NO_CONTENT)
        except GameSession.DoesNotExist:
            context = {
                'error_message': "Такой игры нет."
            }
            return Response(context, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST', 'DELETE'])
def teams(request, pk=0):
    if request.method == 'POST':
        if request.data['method'] == "join":
            username = request.data['username']
            team_name = request.data['team_name']
            try:
                player = Player.objects.get(username=username)
                if player.team != None:
                    context = {
                        'error_message': "Вы уже состоите в команде."
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
                team = Team.objects.get(name=team_name)
                team.players.add(player)
                team.save()
                player.team = team
                player.save()
                serializer = TeamSerializer(team)
                context = {
                    'team': serializer.data
                }
                return Response(context, status=status.HTTP_201_CREATED)
            except Team.DoesNotExist:
                context = {
                    'error_message': 'Такой команды или игрока не существует.'
                }
                return Response(context, status=status.HTTP_404_NOT_FOUND)
        else:
            username = request.data['username']
            team_name = request.data['team_name']
            try:
                player = Player.objects.get(username=username)
                team = Team.objects.get(name=team_name)
                team.players.remove(player)
                team.save()
                player.team = None
                player.save()
                context = {
                    'message': "Игрок убран из команды."
                }
                return Response(context, status=status.HTTP_201_CREATED)
            except Team.DoesNotExist:
                context = {
                    'error_message': 'Такой команды или игрока не существует.'
                }
                return Response(context, status=status.HTTP_404_NOT_FOUND)

