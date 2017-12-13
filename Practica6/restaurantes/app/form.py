from django import forms
from django.core.exceptions import ValidationError

class RestauranteForms(forms.Form):
    barrio = forms.CharField(label='Barrio', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )
