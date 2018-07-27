# Create your views here.
from django.urls import path
from . import views


app_name = 'playermgmt'

urlpatterns = [
    path('<int:league_id>/players', views.players, name='players'),
    path('<int:league_id>/add_player', views.add_player, name='add_player'),
    path('<int:league_id>/<int:player_id>/remove_player/', views.remove_player, name='remove_player'),
]
