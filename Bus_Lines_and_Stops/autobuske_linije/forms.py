from django import forms
from .models import Linija, Stajaliste


class StajalisteForm(forms.ModelForm):
    class Meta:
        model = Stajaliste
        fields = [
            'naziv',
            'ulica',
            'geoSirina',
            'geoDuzina'
            ]
        labels = {
            'geoSirina':'Geogr. širina',
            'geoDuzina':'Geogr. dužina',
            }
        widgets = {
            'geoSirina' : forms.TextInput(attrs={'placeholder':'00.000000'}),
            'geoDuzina' : forms.TextInput(attrs={'placeholder':'00.000000'}),
            }
        
        
class LinijaForm(forms.ModelForm):
    class Meta:
        model = Linija
        fields = [
            'naziv',
            'opis',
            'stajalista',
            ]
        labels = {
            'stajalista':'Stajališta'
            }
        widgets = {
            'opis': forms.Textarea(attrs={'cols': 40, 'rows': 10}),
            'stajalista': forms.CheckboxSelectMultiple(),
        }
