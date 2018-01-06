from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class DeviceModel(models.Model):
    TYPE_TABLET = 'TA'
    TYPE_SMARTPHONE = 'PH'
    TYPE_CHOICES = (
        (TYPE_TABLET, 'Tablet'),
        (TYPE_SMARTPHONE, 'Smartphone'),
    )

    device_type = models.CharField(max_length=2, blank=False, null=False, choices=TYPE_CHOICES, default=TYPE_SMARTPHONE)
    name = models.CharField(max_length=50, blank=False, null=False)
    company = models.ForeignKey('Company', on_delete=models.DO_NOTHING)
    release_year = models.PositiveSmallIntegerField(blank=False, null=False)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

class Device(models.Model):
    color = models.CharField(max_length=50, blank=False, null=False)
    capacity = models.PositiveSmallIntegerField(blank=False, null=False)
    os_version = models.CharField(max_length=50, blank=False, null=False)
    device_model = models.ForeignKey('DeviceModel', on_delete=models.DO_NOTHING)
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s - %s" % (self.device_model, self.capacity, self.color)

