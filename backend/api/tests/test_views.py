from django.test import TestCase

from api.models import (
                Company,
                DeviceModel,
                Device,
            )

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class CompanyViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.company_data = {'name': 'Apple'}
        self.response = self.client.post(
            reverse('create_company'),
            self.company_data,
            format="json")

    def test_api_can_create_a_company(self):
        """Test the api has company creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_read_a_company(self):
        """Test the api has company creation capability."""
        company = Company.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk': company.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, company)

    def test_api_can_update_company(self):
        """Test the api can update a given company."""
        company = Company.objects.get()
        change_company = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': company.id}),
            change_company, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_cannot_update_when_not_company(self):
        """Test the api cannnot update a given company."""
        change_company = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': 9999}),
            change_company, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_can_delete_company(self):
        """Test the api can delete a company."""
        company = Company.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': company.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

class DeviceModelViewTestCase(TestCase):
    """Test suite for the device movel api views."""
    def create_company(self, name="Apple"):
        return Company.objects.create(name=name)

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.device_model_data = {
                                'name'        : 'iPhone 3GS',
                                'release_year': 2010,
                                'device_type' : DeviceModel.TYPE_SMARTPHONE,
                                'company_id'     : self.create_company().id
                            }
        self.response = self.client.post(
            reverse('create_device_model'),
            self.device_model_data,
            format="json")

    def test_api_can_create_a_device_model(self):
        """Test the api has device model creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


class DeviceViewTestCase(TestCase):
    """Test suite for the device api views."""
    def create_company(self, name="Apple"):
        return Company.objects.create(name=name)

    def create_device_model(self, name="iPhone 3GS", release_year=2000, company=None):
        company = self.create_company()
        return DeviceModel.objects.create(name=name, release_year=release_year, company=company)

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.device_data = {
                                'device_model_id' : self.create_device_model().id,
                                'capacity'        : 32,
                                'color'           : 'White',
                                'os_version'      : 'iOS 7'
                            }
        self.response = self.client.post(
            reverse('create_device'),
            self.device_data,
            format="json")

    def test_api_can_create_a_device(self):
        """Test the api has device creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_read_a_device(self):
        """Test the api has device read capability."""
        device = Device.objects.get()
        response = self.client.get(
            reverse('device_details',
                    kwargs={'pk': device.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_device(self):
        """Test the api can update a given device."""
        device = Device.objects.get()
        change_device = self.device_data
        change_device['capacity'] = 64
        res = self.client.put(
            reverse('device_details', kwargs={'pk': device.id}),
            change_device, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_device(self):
        """Test the api can delete a device."""
        device = Device.objects.get()
        response = self.client.delete(
            reverse('device_details', kwargs={'pk': device.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

