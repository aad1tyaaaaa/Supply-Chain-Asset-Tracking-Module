from django import forms
from .models import Asset, Location, AssetLocation

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'description', 'value']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'value': forms.NumberInput(attrs={'step': '0.01'}),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class AssetLocationForm(forms.ModelForm):
    class Meta:
        model = AssetLocation
        fields = ['asset', 'location']
        widgets = {
            'asset': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }
