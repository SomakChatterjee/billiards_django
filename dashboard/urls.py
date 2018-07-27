# Create your views here.
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('lo', views.lo, name='lo'),
    path('player', views.player, name='player'),

    path('player/<int:match_id>/enterscore', views.enterscore, name='enterscore'),
    path('player/completed', views.completed, name='completed'),
    path('player/pending', views.pending, name='pending'),


]
