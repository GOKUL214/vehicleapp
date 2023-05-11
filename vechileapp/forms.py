from .models import Vehicle
from django import forms
class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['number', 'type', 'model', 'description', 'image']
