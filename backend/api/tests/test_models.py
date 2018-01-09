from django.test import TestCase
from api.models import (
                Company,
                DeviceModel,
                Device,
            )

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

class DeviceModelTestCase(TestCase):
    """This class defines the test suite for the Device model."""

    def create_company(self, name="Apple"):
        return Company.objects.create(name=name)

    def create_device_model(self, name="iPhone 3GS", release_year=2000, company=None):
        company = self.create_company()
        return DeviceModel.objects.create(name=name, release_year=release_year, company=company)

    def setUp(self):
        """Define the test client and other test variables."""
        self.color = "Black"
        self.capacity = 32
        self.os_version = "iOS 6"
        self.device_model = self.create_device_model()
        self.device = Device(color=self.color, capacity=self.capacity, os_version=self.os_version, device_model=self.device_model)

    def test_model_can_create_a_device(self):
        """Test the device model can create a device."""
        old_count = Device.objects.count()
        self.device.save()
        new_count = Device.objects.count()
        self.assertNotEqual(old_count, new_count)

