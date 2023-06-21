from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentGetCreate(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    