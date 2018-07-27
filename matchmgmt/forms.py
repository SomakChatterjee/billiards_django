from django.forms import ModelForm
from .models import Match

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ['leagueid','particiapant1_id', 'particiapant2_id','participant1_score','participant2_score']
