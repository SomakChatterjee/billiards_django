# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage




def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phone = form.cleaned_data.get('phone')

            user.is_staff = True
            user.is_active = True
            user.profile.photo = form.cleaned_data.get('photo')


            user.profile.user_type = form.cleaned_data.get('user_type' )
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/dashboard/lo')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

