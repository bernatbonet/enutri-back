from django.contrib.auth.models import Group, User
from rest_framework import viewsets
from apps.security.serializers import GroupSerializer, UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpint that allow groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpint that allow users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
