from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView#, CompanyList

urlpatterns =[
    path('companies/', CreateView.as_view(), name="create"),
    path('companies/<int:pk>', DetailsView.as_view(), name="details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
