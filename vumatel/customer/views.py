from .models import Customer
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Installations to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-created')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
