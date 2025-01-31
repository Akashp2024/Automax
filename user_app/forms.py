from django import forms
from . models import Location,Profile
from django.contrib.auth.models import User
from .widgets import CustomPictureImageFieldWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'username','first_name','last_name'}

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()
    class Meta:
        model = Profile
        fields = {'photo','bio','phone_number'}

class LocationForm(forms.ModelForm):
    address1 = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    class Meta:
        model = Location
        fields = {'address1', 'address2', 'city', 'state', 'zipcode'}

