from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from django.test import TestCase
from .models import Company
# Create your tests here.

class ModelTestCase(TestCase):
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

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.company_data = {'name': 'Apple'}
        self.response = self.client.post(
            reverse('create'),
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

    def test_api_can_delete_company(self):
        """Test the api can delete a company."""
        company = Company.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': company.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
