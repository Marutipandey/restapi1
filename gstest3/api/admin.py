from django.contrib import admin
from .models import rewardss,leaderboard
# Register your models here.
@admin.register(rewardss)
class rewardAdmin(admin.ModelAdmin):
    list_display =['id','amount']


@admin.register(leaderboard)
class leaderboardAdmin(admin.ModelAdmin):
    list_display =['id','point']