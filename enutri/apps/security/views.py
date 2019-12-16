from django.contrib.auth.models import Group, Permission,  User
from rest_framework import viewsets
from apps.security.serializers import GroupSerializer, PermissionSerializer, UserSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpint that allow permissions to be viewed or edited
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

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
