from rest_framework import viewsets
from .models import BaseUser, BaseUserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer