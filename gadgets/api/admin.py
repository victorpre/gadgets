from django.contrib import admin

# Register your models here.

from .models import (
                Company,
                DeviceModel,
                Device,
            )

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    class Meta:
        model = Company

class DeviceModelModelAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "release_year", "created_at", "updated_at"]
    search_fields = ["name"]
    class Meta:
        model = DeviceModel

class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ["device_model", "capacity", "color", "os_version", "created_at", "updated_at"]
    class Meta:
        model = Device

admin.site.register(Company, CompanyModelAdmin)
admin.site.register(DeviceModel, DeviceModelModelAdmin)
admin.site.register(Device, DeviceModelAdmin)
