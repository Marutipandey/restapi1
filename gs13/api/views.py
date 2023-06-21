from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyModel
from .serializers import MyModelSerializer


class MyModelAPIView(APIView):
    def get(self, request):
        queryset = MyModel.objects.all()
        serializer = MyModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            instance = MyModel.objects.get(pk=pk)
        except MyModel.DoesNotExist:
            return Response(status=404)

        serializer = MyModelSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            instance = MyModel.objects.get(pk=pk)
        except MyModel.DoesNotExist:
            return Response(status=404)

        instance.delete()
        return Response(status=204)
