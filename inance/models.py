from django.db import models
from django.db.models import TextField, CharField


# Create your models here.
class AdditionalInformation(models.Model):
    key = CharField(max_length=100, unique=True)
    value = TextField()

    def __str__(self):
        return self.key

class CustomerReviews(models.Model):
    name = CharField(max_length=100)
    image = CharField(max_length=50)
    feedback = TextField()

    def __str__(self):
        return self.name