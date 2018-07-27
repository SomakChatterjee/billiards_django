from django.forms import ModelForm
from .models import League_player

class League_players(ModelForm):
    class Meta:
        model = League_player
        fields = ['leauge_id', 'player_id']

