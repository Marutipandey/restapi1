from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method=='GET':
        id =pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        return Response(serializer.data) 
    
    if request.method=='POST':
         serializer=StudentSerializers(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
         return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    

    if request.method=='PUT':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response({'msg':'Complete Data updated'})
        return Response(serializer.errors )
    
    if request.method=='DELETE':
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})


    if request.method=='PATCH':
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
             serializer.save()
             return Response({'msg':'Partial Data updated'})
        return Response(serializer.errors ) 
         