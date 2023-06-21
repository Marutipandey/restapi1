from .models import student
from rest_framework import serializers


# class StudentSerializerd(serializers.Serializer):

#     student_name=serializers.CharField(max_length=100)
#     student_roll=serializers.IntegerField()

class StudentSerializerd(serializers.ModelSerializer):

     class Meta:
          model=student
          fields=['id','student_name','student_roll']
