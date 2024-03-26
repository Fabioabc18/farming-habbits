from django import forms
from .models import Plant

class PlantChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class PlantSelectionForm(forms.Form):
    plant = PlantChoiceField(queryset=Plant.objects.all(), empty_label=None)
