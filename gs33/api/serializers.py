from .models import Student
from rest_framework import serializers
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id','url','name','city']
    

    