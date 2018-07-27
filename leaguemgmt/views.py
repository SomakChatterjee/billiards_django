from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .forms import leagueForm
from .models import League
from frontendauth.models import Profile
from matchmgmt.models import Match


def league(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()


    if usertype > 0:

        leagues = League.objects.filter(user_id=request.user.id)

        context ={'leagues':leagues,'title': 'Leauge'}

        return render(request,'league.html',context)

    else:
        return redirect('/dashboard/player')

def create(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()

    if usertype > 0:
        form = leagueForm(request.POST or None)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'League Created Successfully.')
                return redirect('/league/')

        errors = form.errors;

        context ={'userid':request.user.id,'errors':errors,'title': 'create Leauge'}

        return render(request,'create.html',context)

    else:
        return redirect('/dashboard/player')


def edit(request,league_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()

    if usertype > 0:
        form = leagueForm(request.POST or None)
        if request.method == 'POST':
            leagues = get_object_or_404(League, pk=league_id)
            leagues.leaguename = request.POST['leaguename']
            leagues.save()
            messages.add_message(request, messages.INFO, 'League Updated Successfully.')
            return redirect('/league/')

        leagues = League.objects.filter(id=league_id)
        for league in leagues:
            leaguename=league.leaguename

        errors = form.errors;

        context ={'leaguename':leaguename,'errors':errors,'title': 'Edit Leauge'}

        return render(request,'edit.html',context)

    else:
        return redirect('/dashboard/player')


def delete(request,league_id):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()

    if usertype > 0:
        countmatc = Match.objects.filter(leagueid=league_id).count()
        if countmatc == 0:
            League.objects.filter(id=league_id).delete()
            messages.add_message(request, messages.INFO, 'League Deleted Successfully.')
        else:
            messages.add_message(request, messages.INFO,
                                 'This League can not be deleted as League has been scheduled for the Match')
        return redirect('/league')
    else:
        return redirect('/dashboard/player')