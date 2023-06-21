from rest_framework import serializers
from .models import rewardss,leaderboard


class amountSerializers(serializers.Serializer):
    class Meta:
        model = rewardss
        fields=['id','amount']


class leaderboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = leaderboard
        fields = '__all__'