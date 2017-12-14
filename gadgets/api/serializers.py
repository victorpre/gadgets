from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Company
        fields = ('id', 'name')
        read_only_fields = ('created_at', 'updated_at')
