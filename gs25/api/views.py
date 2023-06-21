from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle 
from api.throttling import JackRateThrottle


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=MyModel.objects.all()
    serializer_class=MyModelSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # throttle_classes =[AnonRateThrottle,UserRateThrottle]
    throttle_classes =[AnonRateThrottle,JackRateThrottle]




