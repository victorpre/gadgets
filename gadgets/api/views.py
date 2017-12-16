from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer
from .models import Company
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

