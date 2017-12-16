from .models import Company
from django.http import Http404

def get_companies(filters):
    """
    Optionally restricts the returned companys to a given name,
    by filtering against a `name` query parameter in the URL.
    """
    queryset = Company.objects.all()
    name = filters.get('name', None)
    if name is not None:
        queryset = queryset.filter(name__icontains=name)
    return queryset

def get_company(pk):
    """
    Finds a company by its private key (id).
    """
    try:
        return Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        raise Http404

