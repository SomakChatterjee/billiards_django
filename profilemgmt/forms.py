from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from frontendauth.models import  Profile


class SignUpForms(ModelForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.',widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',widget=forms.TextInput(attrs={'class': "form-control"}))
    address = forms.CharField(max_length=500, required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    phone = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class': "form-control"}))
    photo = forms.ImageField(max_length=500, required=False,)
    user_type =forms.CharField(max_length=30,)


    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email', 'address','phone','photo','user_type' )