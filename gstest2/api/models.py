from django.db import models

# Create your models here.
class rewardss(models.Model):
    amount =models.IntegerField()



class leaderboard(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    point=models.IntegerField()