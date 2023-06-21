from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=MyModel.objects.all()
    serializer_class=MyModelSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


