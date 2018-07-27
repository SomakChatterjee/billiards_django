# Create your views here.
from django.urls import path
from . import views

app_name = 'matchmgmt'

urlpatterns = [
    path('<int:league_id>/match', views.match, name='match'),
    path('<int:league_id>/schedule_match', views.schedule_match, name='schedule_match'),
    path('<int:league_id>/<int:match_id>/edit', views.edit, name='edit'),
    path('<int:league_id>/delete/<int:match_id>', views.delete, name='delete'),


]
