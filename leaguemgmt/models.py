from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

# Create your models here.

class League(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    leaguename = models.CharField(max_length=50)


    def __str__(self):
        return '%s' % (self.leaguename)
