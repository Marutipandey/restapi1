from django.shortcuts import render

# Create your views here.
from .models import Student
from rest_framework.response import Response
from .serializers import StudentSerializers
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def hello(request):
    if request.method=='GET':
        data=Student.objects.all()
        serializer =StudentSerializers(data,many=True)
        return Response(serializer.data)
    elif  request.method=='POST':
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201) 
        return Response(serializer.errors, status=400)
    

@api_view(['PUT'])
def hello1(request,pk):
    data=Student.objects.all()
    serializer = StudentSerializers(data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=404)



    
    