from rest_framework import serializers
from .models import Student


    # def start_with_r(value):
    #     if value[0].lower() !='r':
    #          raise serializers.ValidationError('Name should be start width R')
        
class StudentSerializers(serializers.ModelSerializer):

#validators
    def start_width_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('Name Should be start width R')
    name= serializers.CharField (validators=[start_width_r])

    class Meta:
        model=Student
        fields=['name','roll','city']

#field level validators
    def validate_roll(self, value):
        if value>=200:
            raise serializers.ValidationError('Seat Full')
        return value 
    
 # Object Level Validation
    def validate(self, data):
       nm= data.get('name')
       ct=data.get('city')
       if nm.lower() =='rohit' and ct.lower !='ranchi':
           raise serializers.ValidationError('city must be ranchi')
       return data