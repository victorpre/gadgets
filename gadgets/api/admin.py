from django.contrib import admin

# Register your models here.

from .models import Company

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
    search_fields = ["name"]
    class Meta:
        model = Company

admin.site.register(Company, CompanyModelAdmin)
