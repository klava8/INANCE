import django.http
import django.db.models as models
from django.shortcuts import render
from .models import AdditionalInformation

def get_info_by_key(key:str, default_value: str = ""):
    try:
        value = AdditionalInformation.objects.get(key=key).value
        return value
    except AdditionalInformation.DoesNotExist:
        return default_value

# Create your views here.

def main(request: django.http.HttpRequest):
    keys = ('phone_num', 'phone_text')
    info = {
        key: get_info_by_key(key) for key in keys
    }
    return render(request, "index.html", {"info": info})
