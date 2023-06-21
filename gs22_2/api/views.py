from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework import viewsets
from rest_framework .authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=MyModel.objects.all()
    serializer_class=MyModelSerializer
    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]


