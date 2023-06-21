from django.shortcuts import render
from .models import Student
# Create your views here.
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView


class StudentGetCreate(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filterset_fields =['city']
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(pass_by=user)