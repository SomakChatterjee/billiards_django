from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from frontendauth.models import Profile
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from matchmgmt.models import Match
from playermgmt.models import League_player
from leaguemgmt.models import League
from frontendauth.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages

def lo(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()
    if usertype > 0:
        title='Dashboard'
        context ={'title':title}
        return render(request, 'lo.html', context)
    else:
        return redirect('/dashboard/player')

def enterscore(request,match_id):
    if request.method == 'POST':
        match = get_object_or_404(Match, pk=match_id)
        match.participant1_score =request.POST['player1_score']
        match.participant2_score = request.POST['player2_score']
        match.save()
        return redirect('/dashboard/player')

    matches = Match.objects.filter(pk=match_id)
    print(matches)
    matchdetail = []

    for idx, match in enumerate(matches):

        item = {}



        p1 = Profile.objects.filter(user_id=int(match.particiapant1_id))

        for p11 in p1:
            item['p1_fname'] = p11.user.first_name
            item['p1_lname'] = p11.user.last_name
            item['username1'] = p11.user

        p2 = Profile.objects.filter(user_id=int(match.particiapant2_id))

        for p22 in p2:
            item['p2_fname'] = p22.user.first_name
            item['p2_lname'] = p22.user.last_name
            item['username2'] = p22.user

        matchdetail.append(item);

    title = 'Player Score'
    context = {'title': title, 'matchdetail':matchdetail}
    return render(request, 'player_score.html', context)



def player(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='player').count()

    if usertype > 0:

        matches = Match.objects.filter(Q(particiapant1_id=request.user.id) | Q(particiapant2_id=request.user.id))


        matchdetail = []

        for idx, match in enumerate(matches):


            item = {}
            item['match_id'] = match.id
            item['match_leaguename'] = match.leagueid.leaguename

            #print( League.objects.filter('leaguename').get(pk=match.leagueid))
            item['can_modify'] = match.participant1_score + match.participant2_score


            item['participant1_score'] = match.participant1_score
            item['participant2_score'] = match.participant2_score
            p1 = Profile.objects.filter(user_id=int(match.particiapant1_id))

            for p11 in p1:
                item['p1_fname'] = p11.user.first_name
                item['p1_lname'] = p11.user.last_name



            p2 = Profile.objects.filter(user_id=int(match.particiapant2_id))

            for p22 in p2:
                item['p2_fname'] = p22.user.first_name
                item['p2_lname'] = p22.user.last_name

            matchdetail.append(item);


        title='Dashboard'
        context ={'title':title,'matches':matchdetail,}
        return render(request,'player.html',context)

    else:
        return redirect('/dashboard/lo')


def completed(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='player').count()

    if usertype > 0:

        matches = Match.objects.filter(Q(particiapant1_id=request.user.id) | Q(particiapant2_id=request.user.id))

        matchdetail = []

        for idx, match in enumerate(matches):
            item = {}
            score = match.participant1_score + match.participant2_score
            if score>0 :
                item['can_modify'] = match.participant1_score + match.participant2_score

                item['match_id'] = match.id
                item['match_leaguename'] = match.leagueid.leaguename
                item['participant1_score'] = match.participant1_score
                item['participant2_score'] = match.participant2_score

                # print( League.objects.filter('leaguename').get(pk=match.leagueid))


                p1 = Profile.objects.filter(user_id=int(match.particiapant1_id))

                for p11 in p1:
                    item['p1_fname'] = p11.user.first_name
                    item['p1_lname'] = p11.user.last_name

                p2 = Profile.objects.filter(user_id=int(match.particiapant2_id))

                for p22 in p2:
                    item['p2_fname'] = p22.user.first_name
                    item['p2_lname'] = p22.user.last_name

                matchdetail.append(item);

        title = 'Matches'
        context = {'title': title, 'matches': matchdetail, }
        return render(request, 'player.html', context)

    else:
        return redirect('/dashboard/lo')


def pending(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='player').count()

    if usertype > 0:

        matches = Match.objects.filter(Q(particiapant1_id=request.user.id) | Q(particiapant2_id=request.user.id))

        matchdetail = []

        for idx, match in enumerate(matches):
            item = {}
            score = match.participant1_score + match.participant2_score
            if score == 0:
                item['can_modify'] = match.participant1_score + match.participant2_score

                item['match_id'] = match.id
                item['match_leaguename'] = match.leagueid.leaguename

                # print( League.objects.filter('leaguename').get(pk=match.leagueid))

                p1 = Profile.objects.filter(user_id=int(match.particiapant1_id))

                for p11 in p1:
                    item['p1_fname'] = p11.user.first_name
                    item['p1_lname'] = p11.user.last_name

                p2 = Profile.objects.filter(user_id=int(match.particiapant2_id))

                for p22 in p2:
                    item['p2_fname'] = p22.user.first_name
                    item['p2_lname'] = p22.user.last_name

                matchdetail.append(item);

        title = 'Matches'
        context = {'title': title, 'matches': matchdetail, }
        return render(request, 'player.html', context)

    else:
        return redirect('/dashboard/lo')

