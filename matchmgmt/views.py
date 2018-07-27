from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from .forms import MatchForm
from .models import Match
from playermgmt.models import League_player
from leaguemgmt.models import League
from frontendauth.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages

def match(request,league_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        matches = Match.objects.filter(leagueid=league_id)
        matchdetail = []

        for idx, match in enumerate(matches):

            item = {}
            item['match_id'] = match.id
            item['participant1_score'] = match.participant1_score
            item['participant2_score'] = match.participant2_score

            item['can_modify'] = match.participant1_score +  match.participant2_score

            p1 = Profile.objects.filter(user_id=int(match.particiapant1_id))
            
            for p11 in p1:
                item['p1_fname']= p11.user.first_name
                item['p1_lname']= p11.user.last_name


            p2 = Profile.objects.filter(user_id=int(match.particiapant2_id))

            for p22 in p2:
                item['p2_fname']= p22.user.first_name
                item['p2_lname']= p22.user.last_name


            matchdetail.append(item);

        #print(matchdetail)
        context ={'matches':matchdetail,'league_id':league_id,'breadcamp':'Match'}
        return render(request,'match.html',context)
    else:
        return redirect('/dashboard/player')


def schedule_match(request,league_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        form = MatchForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'Match Scheduled Successfully.')
                return redirect('/match/' + str(league_id) + '/match')

        errors = form.errors;

        title = League.objects.filter(pk=league_id).values('leaguename')
        players = League_player.objects.filter(leauge_id=league_id)

        print(players)
        context ={'league_id':title,'errors':errors,'players':players,'league_id': league_id,'breadcamp':'Schedule Match'}
        return render(request,'schedule_match.html',context)
    else:
        return redirect('/dashboard/player')

def edit(request,league_id,match_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        form =  MatchForm(request.POST or None)
        if request.method == 'POST':
            matches = get_object_or_404(League, pk=league_id)
            matches.leaguename = request.POST['leaguename']
            matches.save()
            messages.add_message(request, messages.INFO, 'Match Updated Successfully.')
            return redirect('/league/')

        matches = League_player.objects.filter(id=league_id)
        print (matches)
        for league in leagues:
            leaguename = league.leaguename
        return render(request,'edit.html',context)
    else:
        return redirect('/dashboard/player')

def delete(request,league_id,match_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:

        Match.objects.filter(id=match_id).delete()
        messages.add_message(request, messages.INFO, 'Match Deleted Successfully.')
        return redirect('/match/' + str(league_id) + '/match')

    else:
        messages.add_message(request, messages.INFO, 'Unable to delete the Match ')
        return redirect('/dashboard/player')













