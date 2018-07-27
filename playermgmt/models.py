from django.db import models
from leaguemgmt.models import League
from django.contrib.auth.models import User

# Create your models here.

class League_player(models.Model):
    leauge_id = models.ForeignKey(League,on_delete=models.CASCADE)
    player_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.leauge_id, self.player_id)
