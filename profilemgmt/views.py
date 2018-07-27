
from django.http import Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404,redirect

from leaguemgmt.models import League
from django.contrib.auth import login, authenticate
from frontendauth.models import Profile
from django.contrib.auth.models import User
from .forms import SignUpForms as SignUpForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views

# Create your views here.

def lo(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='lo').count()

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = get_object_or_404(User, pk=request.POST['userid'])
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            user.refresh_from_db()

            profile = get_object_or_404(Profile, pk=request.POST['profile_id'])
            profile.address = request.POST.get('address')
            profile.phone = request.POST.get('phone')
            if (form.cleaned_data.get('photo')):
                profile.photo=  form.cleaned_data.get('photo')
            profile.save()
            if usertype > 0:

                return redirect('/dashboard/lo',)
            else:
                return redirect('/dashboard/player', )
        else:
            print(form.errors)
            return redirect('/profile/lo')



    user = get_object_or_404(User, pk=request.user.id)
    try:
        profilee = get_object_or_404(Profile, user_id=request.user.id)

    except(KeyError, Profilee.DoesNotExist):
        return redirect('/')
    else:
        title = 'lo'
        context = {'title': title,
                   'username': user.username,
                   'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'id': profilee.id,
                   'user_id': profilee.user_id,
                   'address': profilee.address,
                   'phone': profilee.phone,
                   'user_type': profilee.user_type,
                   'photo': profilee.photo,
                   'usertype' : usertype

                }

        return render(request, 'lo_player.html', context)

    return redirect('/')

## Change password

def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():


            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')

            return render(request, 'change_passworddd.html', {'form': form})
        else:

            form = PasswordChangeForm(request.user)

            return render(request, 'change_passworddd.html',{'form': form})
    else:
        form = PasswordChangeForm(request.user)

        return render(request, 'change_passworddd.html', {'form': form})

def player(request):
    usertype = Profile.objects.filter(user_id=request.user.id).filter(user_type='player').count()

    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            user = get_object_or_404(User, pk=request.POST['userid'])
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            user.refresh_from_db()

            profile = get_object_or_404(Profile, pk=request.POST['profile_id'])
            profile.address = request.POST.get('address')
            profile.phone = request.POST.get('phone')
            if(form.cleaned_data.get('photo')):
                profile.photo = form.cleaned_data.get('photo')
            profile.save()


            return redirect('/dashboard/player', )

        else:
            print(form.errors)
            return redirect('/profile/player')

    user = get_object_or_404(User, pk=request.user.id)
    try:
        profilee = get_object_or_404(Profile, user_id=request.user.id)

    except(KeyError, Profilee.DoesNotExist):
        return redirect('/')
    else:
        title = 'lo'
        context = {'title': title,
                   'username': user.username,
                   'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'id': profilee.id,
                   'user_id': profilee.user_id,
                   'address': profilee.address,
                   'phone': profilee.phone,
                   'user_type': profilee.user_type,
                   'photo': profilee.photo,
                   'usertype': usertype

                   }

        return render(request, 'lo_player_editprofile.html', context)

    return redirect('/')


def lo_action(request):
    title='LO Submit'
    context ={'title':title}
    return render(request,'lo_action.html',context)

def player_action(request):
    title='Player Submit'
    context ={'title':title}
    return render(request,'player_action.html',context)


