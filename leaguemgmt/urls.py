# Create your views here.
from django.urls import path
from . import views

app_name = 'leaguemgmt'

urlpatterns = [
    path('', views.league, name='league'),
    path('create', views.create, name='create'),
    path('<int:league_id>/edit', views.edit, name='edit'),
    path('<int:league_id>/delete', views.delete, name='delete'),

]
