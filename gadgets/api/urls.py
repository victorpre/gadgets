from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView#, CompanyList

urlpatterns =[
    path('companies/', CompanyListCreateView.as_view(), name="create"),
    path('companies/<int:pk>', CompanyRetrieveUpdateDestroyView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
