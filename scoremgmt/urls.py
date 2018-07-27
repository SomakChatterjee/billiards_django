# Create your views here.
from django.urls import path
from . import views

app_name = 'scoremgmt'

urlpatterns = [
    path('<int:league_id>/scoreboard', views.scoreboard, name='scoreboard'),
    path('<int:match_id>/enter_score', views.enter_score, name='enter_score'),
    path('<int:match_id>/enter_score_action', views.enter_score_action, name='enter_score_action'),
]
