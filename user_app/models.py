from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
from django.core.validators import RegexValidator
from .utils import user_directory_path
# from localflavor.in_.forms import INZipCodeField as INZipCodeValidator
# Create your models here.

class Location(models.Model):
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = INStateField( default = 'KL')    
    zipcode = models.CharField(
        max_length=6,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',
                message="Enter a valid 6-digit ZIP code."
            )
        ],
        help_text="Enter a valid 6-digit Indian postal code."
    )

    def __str__(self):
        return f'Location-{self.id}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}-Profile'
    