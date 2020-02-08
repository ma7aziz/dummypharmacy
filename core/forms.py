from django.forms import ModelForm
from . import models


class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['phone', 'birthdate', 'address1', 'address2', 'address3']
