from django.urls import path
from . import views

urlpatterns = [
    path('main_lobby/', views.main_lobby, name = 'main_lobby'),
    path('game_lobby', views.game_lobby, name = 'game_lobby'),
]
