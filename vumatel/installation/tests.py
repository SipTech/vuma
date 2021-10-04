from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from vumatel.installation.models import (Installation, InstallationStatus)
from django.contrib.auth.models import User
from vumatel.customer.models import Customer


class InstallationTests(APITestCase):
    def test_create_init(self):
        """
        Create initial data
        """
        url = 'installations'
        user = User.objects.create_user(username='testInstaller', password='12345')
        installer = self.client.login(username='testInstaller', password='12345')
        customer = Customer.objects.create(first_name='Sipho', last_name='Mkhwanazi', email='sipho.mkhwanazi@vumatel.co.za')
        installation_status = Installation.objects.create(name='Requested', color='white')

        data = {'user': installer.url, 'customer': customer.url, 'color': installation_status.url}
        # Create installation request
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Installation.objects.count(), 1)
        self.assertEqual(Installation.objects.get().customer.id, customer.id)

    def test_update_installation_in_progress(self):
        """
        Update stallation status in progress
        """
        customer = Customer.objects.get(first_name="Sipho")
        installation = Installation.get(pk=customer.id)
        installation_status = InstallationStatus.objects.create(name="In Progress", color="yellow")
        url = reverse('installations/{0}/'.format(installation.id))
        data = {'status': installation_status.id}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_installation_complete(self):
        """
        Update stallation status in progress
        """
        customer = Customer.objects.get(first_name="Sipho")
        installation = Installation.get(pk=customer.id)
        installation_status = InstallationStatus.objects.create(name="Complete", color="green")
        url = reverse('installations/{0}/'.format(installation.id))
        data = {'status': installation_status.id}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_installation_rejected(self):
        """
        Update stallation status rejected
        """
        customer = Customer.objects.get(first_name="Sipho")
        installation = Installation.get(pk=customer.id)
        installation_status = InstallationStatus.objects.create(name="Rejected", color="red")
        url = reverse('installations/{0}/'.format(installation.id))
        data = {'status': installation_status.id}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)