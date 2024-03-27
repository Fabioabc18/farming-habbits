from django import forms
from django.core.validators import MinValueValidator
from .models import WaterConsumption

class WaterConsumptionForm(forms.ModelForm):
    amount = forms.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        model = WaterConsumption
        fields = ['amount']
