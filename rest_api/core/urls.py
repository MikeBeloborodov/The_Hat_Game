from django.urls import path, include
from . import views

urlpatterns = [
    path('player/', views.player, name="player"),
    path('player_logout/', views.player_logout, name='logout'),
    path('game_session/', views.game_session, name='session'),
]
