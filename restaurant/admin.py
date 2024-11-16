from django.contrib import admin
from .models import AdditionalInformation

# Register your models here.
@admin.register(AdditionalInformation)
class AdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')