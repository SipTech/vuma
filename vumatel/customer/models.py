from django.db import models


class Customer(models.Model):
	first_name = models.CharField(blank=False, null=False, max_length=100)
	last_name = models.CharField(blank=False, null=False, max_length=100)
	email = models.EmailField(blank=False, null=False, max_length=100, unique=True)
	created = models.DateTimeField(auto_now_add=True, blank=True)
	modified = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		name = "{0} - {1}".format(self.first_name, self.last_name)
		return name

	class Meta:
		managed = True
		db_table = 'customer'
		verbose_name_plural = "Customers"
