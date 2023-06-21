from django.shortcuts import render
from .models import student
from rest_framework.permissions import  IsAuthenticated
# Create your views here.
from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializerd


class StudentGetCreate(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=StudentSerializerd
    
class StudentUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= student.objects.all()
    serializer_class =StudentSerializerd
    permission_classes=[IsAuthenticated]
