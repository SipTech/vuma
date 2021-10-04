from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('installations', views.InstallationViewSet)
router.register('installation-statuses', views.InstallationStatusViewSet)

urlpatterns = [
	path('', include(router.urls)),
]
