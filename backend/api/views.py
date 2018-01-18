from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
                    CompanySerializer,
                    DeviceModelSerializer,
                    DeviceSerializer,
                )

from .models import (
                Company,
                DeviceModel,
                Device,
            )

from . import company_service

class CompanyListCreateView(APIView):
    """This class defines the create behavior of our rest api."""

    def get(self, request, format=None):
        """Retrieves the list of companies. """
        companies = company_service.get_companies(request.query_params)
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        """Save the post data when creating a new company."""
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyRetrieveUpdateDestroyView(APIView):
    """This class handles the http GET, PUT and DELETE requests."""

    def get(self, request, pk, format=None):
        """Retrieves a single company."""
        company = company_service.get_company(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Updates a single company record."""
        company = company_service.get_company(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Deletea single company record."""
        company = company_service.get_company(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DeviceModelListCreateView(APIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = DeviceModelSerializer

    def get(self, request, format=None):
        """Retrieves the list of device models. """
        device_models = DeviceModel.objects.all()
        serializer = DeviceModelSerializer(device_models, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        """Save the post data when creating a new device model."""
        serializer = DeviceModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceListCreateView(APIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = DeviceSerializer

    def get(self, request, format=None):
        """Retrieves the list of devices. """
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        """Save the post data when creating a new device."""
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceRetrieveUpdateDestroyView(APIView):
    """This class handles the http GET, PUT and DELETE requests."""
    serializer_class = DeviceSerializer

    def get_object(self, pk):
        try:
            return Device.objects.get(pk=pk)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Updates a single device record."""
        device = self.get_object(pk)
        serializer = DeviceSerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        """Delete a single device record."""
        device = Device.objects.get(pk=pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


