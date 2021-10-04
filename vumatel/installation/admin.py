from django.contrib import admin

from .models import (
	InstallationStatus,
	Installation,
)

installation_models = [
	InstallationStatus,
	Installation,
]

admin.site.register(installation_models)
