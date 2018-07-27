# Create your views here.
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'profilemgmt'

urlpatterns = [
    path('lo', views.lo, name='lo'),
    path('player', views.player, name='player'),
    path('lo_action', views.lo_action, name='lo_action'),
    path('player_action', views.player_action, name='player_action'),
    path('changepassword', views.changepassword, name='changepassword'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
