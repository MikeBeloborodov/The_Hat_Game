from django.urls import path, include
from . import views

urlpatterns = [
    path('player/', views.player, name="player"),
]
