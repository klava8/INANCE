from django.contrib import admin
from .models import AdditionalInformation
from .models import CustomerReviews

# Register your models here.
admin.site.register(AdditionalInformation)
admin.site.register(CustomerReviews)

class AdditionalInformationAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

class CustomerReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'stars', 'feedback')
