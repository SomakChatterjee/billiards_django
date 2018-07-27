from django.db import models
from leaguemgmt.models import League


class Match(models.Model):
    leagueid = models.ForeignKey(League,on_delete=models.CASCADE)
    particiapant1_id = models.IntegerField()
    particiapant2_id = models.IntegerField()
    participant1_score = models.IntegerField()
    participant2_score = models.IntegerField()

    def __str__(self):
        return '%s' % (
        self.leagueid)




