from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView


class StudentListCreate(ListCreateAPIView):
    queryset=MyModel.objects.all()
    serializer_class=MyModelSerializer


class StudentRetriveUpdate(DestroyAPIView):
    queryset=MyModel.objects.all()
    serializer_class=MyModelSerializer
