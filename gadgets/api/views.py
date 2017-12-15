from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
    )
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer
from .models import Company

from . import company_service

#   class CompanyList(APIView):
#      """
#      List all companies, or create a new company.
#      """
#      def get(self, request, format=None):
#          companies = Company.objects.all()
#          serializer = CompanySerializer(companies, many=True)
#          return Response(serializer.data)
#
#      def post(self, request, format=None):
#          serializer = CompanySerializer(data=request.data)
#          if serializer.is_valid():
#              serializer.save()
#              return Response(serializer.data, status=status.HTTP_201_CREATED)
#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyListCreateView(ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Optionally restricts the returned companys to a given name,
        by filtering against a `name` query parameter in the URL.
        """
        return company_service.get_companies(self.request.query_params)

    def perform_create(self, serializer):
        """Save the post data when creating a new company."""
        serializer.save()

class DetailsView(RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
