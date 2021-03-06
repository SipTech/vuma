from django.contrib.auth.models import User
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser', 'date_joined']