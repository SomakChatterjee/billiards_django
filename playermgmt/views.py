from django.http import Http404,HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from frontendauth.models import  Profile
from .models import League_player
from .forms import League_players
from leaguemgmt.models import League
from django.db.models import Q
from django.contrib import messages
from matchmgmt.models import Match
from frontendauth.models import Profile
from pprint import pprint
# Create your views here.

def players(request,league_id):
    leagueid =league_id

    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        title = League.objects.filter(pk=league_id).values('leaguename')
        players = League_player.objects.filter(leauge_id=leagueid)

        context ={'players':players,'title' :title ,'league_id' :leagueid,'breadcamp':'Matches'}
        return render(request,'players.html',context)
    else:
        return redirect('/dashboard/lo')

def add_player(request,league_id):
    leagueid = league_id
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        if request.method == 'POST':

            for group_location in request.POST.getlist('player_id[]'):
                league_player = League_player(player_id = User.objects.get(pk=group_location),leauge_id = League.objects.get(pk=leagueid))
                league_player.save()

                #form.save()
            messages.add_message(request, messages.INFO, 'Player added Successfully.')
            return redirect('/player/'+str(leagueid)+'/players')

        players = League_player.objects.filter(leauge_id=leagueid)

        players = [paticipentPlayer.player_id.id for paticipentPlayer in players]
        playerdeatils = Profile.objects.filter(user_type='player').exclude(user__in=players)

        context = {'playerdeatils': playerdeatils , 'leagueid' :leagueid,'breadcamp':'Add Players'}
        return render(request, 'add_player.html', context)
    else:
        return redirect('/dashboard/lo')




def remove_player(request,league_id,player_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:

        countmatc = Match.objects.filter(particiapant1_id=player_id).filter(particiapant2_id=player_id).count()
        if countmatc == 0:
            messages.add_message(request, messages.INFO, 'Player Deleted Successfully.')
            League_player.objects.filter(player_id=player_id).delete()
        else:
            messages.add_message(request, messages.INFO, 'This Match can not be deleted as match has been scheduled for the player')



        return redirect('/player/' + str(league_id) + '/players')
    else:
        return redirect('/dashboard/lo')