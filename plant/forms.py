from django import forms
from .models import Plant


class PlantSelectionForm(forms.Form):
    plant = forms.ModelChoiceField(queryset=Plant.objects.all(), empty_label=None)
