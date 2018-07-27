from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
# Create your views here.

def scoreboard(request,league_id):
    title='Score Board'
    context ={'title':title}
    return render(request,'scoreboard.html',context)

def enter_score(request,match_id):
    title='Enter Score'
    context ={'title':title}
    return render(request,'enter_score.html',context)

def enter_score_action(request,match_id):
    title='Enter Score Submit'
    context ={'title':title}
    return render(request,'enter_score_action.html',context)