from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers


@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
    if request.method=='GET':
        id =request.data.get('id')
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
             return Response({'msg':'Data Created'})
         return Response(serializer.errors )
    

    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializers(stu,data=request.data,partial=True)
        if serializer.is_valid():
             serializer.save()
             return Response({'msg':'Data updated'})
        return Response(serializer.errors )
    
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})
    
         