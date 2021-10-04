from django.contrib import admin

from .models import (
	Customer,
)

customer_models = [
	Customer,
]

admin.site.register(customer_models)
