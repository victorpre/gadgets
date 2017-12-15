from .models import Company

def get_companies(filters):
    queryset = Company.objects.all()
    name = filters.get('name', None)
    if name is not None:
        queryset = queryset.filter(name__icontains=name)
    return queryset
