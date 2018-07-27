from django.forms import ModelForm
from .models import League

class leagueForm(ModelForm):
    class Meta:
        model = League
        fields = ['user_id', 'leaguename']
