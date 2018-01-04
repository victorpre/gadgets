from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Company
from .models import DeviceModel

class CompanyModelTestCase(TestCase):
    """This class defines the test suite for the Company model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.company_name = ""
        self.company = Company(name=self.company_name)

    def test_model_can_create_a_company(self):
        """Test the company model can create a company."""
        old_count = Company.objects.count()
        self.company.save()
        new_count = Company.objects.count()
        self.assertNotEqual(old_count, new_count)

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

class DeviceModelModelTestCase(TestCase):
    """This class defines the test suite for the DeviceModel model."""

    def create_company(self, name="Apple"):
        return Company.objects.create(name=name)

    def setUp(self):
        """Define the test client and other test variables."""
        company = self.create_company()
        self.device_model_name = "iPhone 3GS"
        self.release_year = 2000
        self.device_model = DeviceModel(name=self.device_model_name, release_year=self.release_year, company=company)

    def test_model_can_create_a_device_model(self):
        """Test the device_model model can create a device model."""
        old_count = DeviceModel.objects.count()
        self.device_model.save()
        new_count = DeviceModel.objects.count()
        self.assertNotEqual(old_count, new_count)

class DeviceModelViewTestCase(TestCase):
    """Test suite for the company api views."""
    def create_company(self, name="Apple"):
        return Company.objects.create(name=name)

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.company_data = {
                                'name'        : 'iPhone 3GS',
                                'release_year': 2010,
                                'device_type' : DeviceModel.TYPE_SMARTPHONE,
                                'company'     : self.create_company().id
                            }
        self.response = self.client.post(
            reverse('create_device_model'),
            self.company_data,
            format="json")

    def test_api_can_create_a_device_model(self):
        """Test the api has device model creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
