from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializers
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

