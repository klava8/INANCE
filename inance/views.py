from django.shortcuts import render
from .models import AdditionalInformation, CustomerReviews

# Create your views here
def index(request):
    keys = ('phone_num', 'mail', 'location', 'location_link')
    info = {
        key: AdditionalInformation.objects.get(key=key).value for key in keys
    }
    clients = CustomerReviews.objects.all()
    return render(request, 'index.html', {"info": info, "clients": clients})