from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.Serializer):
        name=serializers.CharField(max_length=100)

        def create(self, validated_data):
             return Student.objects.create(**validated_data)
        
        def update(self, instance, validated_data):
               instance.name = validated_data.get("name")
               instance.save()
               return instance