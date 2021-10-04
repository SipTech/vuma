from .models import (Installation, InstallationStatus)
from rest_framework import serializers


class InstallationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Installation
        fields = ['id', 'url', 'installer', 'customer', 'status', 'appointment_date', 'last_modified']


class InstallationStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InstallationStatus
        fields = ['id', 'url', 'name', 'color', 'date_created', 'date_modified']