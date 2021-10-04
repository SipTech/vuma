from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer


class InstallationStatus(models.Model):
	COLOURS = [
		('White', 'white'),
		('Yellow', 'yellow'),
		('Green', 'green'),
		('Red', 'red'),
	]
	STATUSES = [
		('Installation requested', 'Requested'),
		('Installation in progress', 'In Progress'),
		('Installation Complete', 'Complete'),
		('Installation Rejected', 'Rejected')
	]
	name = models.CharField(choices=STATUSES, blank=False, null=False, max_length=100)
	color = models.CharField(choices=COLOURS, blank=False, null=False, max_length=100)
	description = models.TextField(blank=True, null=True, max_length=255)
	date_created = models.DateTimeField(auto_now_add=True, blank=True)
	date_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		name = "{0} - {1}".format(self.name, self.color)
		return name

	class Meta:
		managed = True
		db_table = 'installationStatus'
		verbose_name_plural = 'InstallationStatuses'


class Installation(models.Model):
	installer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	status = models.ForeignKey(InstallationStatus, on_delete=models.SET_NULL, null=True)
	appointment_date = models.DateTimeField(auto_now_add=True, blank=True)
	last_modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		name = "{0} - {1}".format(self.installer, self.customer)
		return name

	class Meta:
		managed = True
		db_table = 'installation'
		verbose_name_plural = 'Installations'
