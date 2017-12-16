from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView
    )

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer
from .models import Company

from . import company_service

class CompanyListCreateView(APIView):
    """This class defines the create behavior of our rest api."""

    def get(self, request, format=None):
        """
        Optionally restricts the returned companys to a given name,
        by filtering against a `name` query parameter in the URL.
        """

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


class DetailsView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
