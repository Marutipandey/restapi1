from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StudentGetCreate(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # filter_backends=[DjangoFilterBackend]
    filter_backends=[SearchFilter]
    # filterset_fields =['name','city']
    search_fields =['name','city']

   