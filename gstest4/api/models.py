from django.db import models

# Create your models here.
class rewardss(models.Model):
    amount =models.IntegerField()



class leaderboard(models.Model):
    name=models.CharField(max_length=100,default="hello")
    point = models.IntegerField()
    # Other fields and methods
