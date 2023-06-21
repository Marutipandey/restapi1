from rest_framework import serializers
from .models import rewardss


class amountSerializers(serializers.Serializer):
    class Meta:
        model = rewardss
        fields=['id','amount']