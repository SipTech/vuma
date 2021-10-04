from .models import Installation, InstallationStatus
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import InstallationSerializer, InstallationStatusSerializer


class InstallationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Installations to be viewed or edited.
    """
    queryset = Installation.objects.all().order_by('-appointment_date')
    serializer_class = InstallationSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstallationStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Installations Statuses to be viewed or edited.
    """
    queryset = InstallationStatus.objects.all()
    serializer_class = InstallationStatusSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
