from django.shortcuts import render
from .models import AdditionalInformation

def find_info(key: str, default_value: str = ""):
    try:
        value = AdditionalInformation.objects.get(key=key).value
        return value
    except AdditionalInformation.DoesNotExist:
        return default_value

# Create your views here
def index(request):
    keys = ('phone_num', 'mail', 'location', 'location_link')
    info = {
        key: find_info(key) for key in keys
    }
    return render(request, 'index.html', {"info": info})