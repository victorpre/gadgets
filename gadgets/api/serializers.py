from rest_framework import serializers
from rest_framework.serializers import (
                                    SerializerMethodField,
                                    PrimaryKeyRelatedField,
                                )
from .models import (
                Company,
                DeviceModel,
            )

class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id', 'name')
        read_only_fields = ('created_at', 'updated_at')

class DeviceModelSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    device_type = SerializerMethodField()
    company_id = PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company', label="Company")
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = DeviceModel
        fields = ('id', 'name', 'company_id', 'release_year', 'device_type')
        read_only_fields = ('created_at', 'updated_at')

    def get_device_type(self, obj):
        return obj.get_device_type_display()
