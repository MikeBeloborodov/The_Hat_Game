from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Player, Team, GameSession
from .serializers import PlayerSerializer, TeamSerializer, GameSessionSerializer

@api_view(['GET', 'POST', 'DELETE'])
def player(request, pk=0):
    if request.method == 'POST':
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
        
