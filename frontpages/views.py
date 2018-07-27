from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from matchmgmt.models import Match
from playermgmt.models import League_player
from leaguemgmt.models import League
from frontendauth.models import Profile


def index(request):

    title='HOME PAGE'
    matches = Match.objects.filter(participant1_score=0).filter(participant2_score=0)
    matchdetail = []
    for idx, match in enumerate(matches):

        item = {}
        item['match_id'] = match.id

        item['leaguename'] = match.leagueid
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

    context ={'title':title,'matches':matchdetail}

    return render(request,'index.html',context)