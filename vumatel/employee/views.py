from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Installations to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]