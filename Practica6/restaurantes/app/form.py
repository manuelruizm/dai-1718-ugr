from django import forms
from django.core.exceptions import ValidationError

class RestauranteForms(forms.Form):
    barrio = forms.CharField(label='Barrio', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )

class AnadirRestForms(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=60, strip=True, required=False,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )
    barrio = forms.CharField(label='Barrio', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )

class ModificarForms(forms.Form):
    iden = forms.CharField(label='ID', max_length=60, strip=True, required=False,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )
    nombre = forms.CharField(label='Nombre', max_length=60, strip=True, required=False,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )
    cocina = forms.CharField(label='Cocina', max_length=60, strip=True, required=False,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )

class MapaForms(forms.Form):
    ident = forms.CharField(label='ID', max_length=60, strip=True,
                             widget=forms.TextInput(
                                attrs={'class':'form-control text-muted col-md-4',
                                       'size':30,
                                       })
                                    )
