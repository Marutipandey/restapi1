from rest_framework import serializers
from .models import rewardss,leaderboard


class amountSerializers(serializers.Serializer):
    class Meta:
        model = rewardss
        fields=['id','amount']


class leaderboardSerializers(serializers.Serializer):
    class Meta:
        model = rewardss
        fields=['id','name','roll','point']
