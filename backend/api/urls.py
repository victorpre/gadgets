from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
                CompanyListCreateView,
                CompanyRetrieveUpdateDestroyView,
                DeviceModelListCreateView,
                DeviceListCreateView,
            )

urlpatterns =[
    path('companies/', CompanyListCreateView.as_view(), name="create_company"),
    path('companies/<int:pk>', CompanyRetrieveUpdateDestroyView.as_view(), name="details"),
    path('device_models/', DeviceModelListCreateView.as_view(), name="create_device_model"),
    path('devices/', DeviceListCreateView.as_view(), name="create_device"),
]

urlpatterns = format_suffix_patterns(urlpatterns)