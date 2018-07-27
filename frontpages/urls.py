# Create your views here.
from django.urls import path
from . import views

app_name = 'frontpages'

urlpatterns = [
    path('', views.index, name='index'),

]
