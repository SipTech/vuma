"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('installation/', include('installation.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
"""

from django.urls import include, path
from rest_framework import routers
from installation.views import InstallationViewSet, InstallationStatusViewSet
from customer.views import CustomerViewSet
from employee.views import EmployeeViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'installations', InstallationViewSet)
router.register(r'installation-statuses', InstallationStatusViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'users', EmployeeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]