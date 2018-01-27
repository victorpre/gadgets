from .models import Device
from django.http import Http404

def get_devices(filters={}):
    """
    Optionally restricts the returned companys to a given name,
    by filtering against a `name` query parameter in the URL.
    """
    queryset = Device.objects.all()

    device_model_id = filters.get('device_model_id', None)
    capacity = filters.get('capacity', None)
    color = filters.get('color', None)
    os_version = filters.get('os_version', None)
    if device_model_id is not None:
        queryset = queryset.filter(device_model_id=device_model_id)
    if capacity is not None:
        queryset = queryset.filter(capacity=capacity)
    if color is not None:
        queryset = queryset.filter(color__icontains=color)
    if os_version is not None:
        queryset = queryset.filter(os_version__icontains=os_version)
    return queryset

def get_device(pk):
    """
    Finds a device by its private key (id).
    """
    try:
        return Device.objects.get(pk=pk)
    except Device.DoesNotExist:
        raise Http404

