from rest_framework import status
from rest_framework.test import APITestCase
from vumatel.customer.models import Customer

class CustomerTests(APITestCase):
	def test_create_customer(self):
		"""
		Test customer creation
		"""
		url = "users"
		data = {'first_name':'Sipho', 'last_name':'Mkhwanazi', 'email':'sipho.mkhwanazi@vumatel.co.za'}
		# Create installation request
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_update_customer(self):
		"""
		Test customer information update
		"""
		url = "users/1/"
		data = {'first_name':'Sipho2'}
		# Create installation request
		response = self.client.patch(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_delete_customer(self):
		"""
		Test customer information update
		"""
		url = "users/1/"
		# Create installation request
		response = self.client.delete(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
