from django.shortcuts import render
from .models import rewardss
from .serializers import amountSerializers
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum



# class CountView(APIView):
#     def get(self, request):
#         total_count = rewardss.objects.count()
#         return Response({'total_count': total_count})


class CountView(APIView):
    def get(self, request):
        total_amount = rewardss.objects.aggregate(total_amount=Sum('amount'))['total_amount']
        return Response({'total_amount': total_amount})