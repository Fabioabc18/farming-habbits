from django import forms
from django.core.validators import MinValueValidator
from .models import CaloriesConsumption

class CaloriesConsumptionForm(forms.ModelForm):
    amount = forms.FloatField(validators=[MinValueValidator(0)])

    class Meta:
        model = CaloriesConsumption
        fields = ['amount']
