from django import forms
from .models import WaterConsumption

class WaterConsumptionForm(forms.ModelForm):
   class Meta:
       model = WaterConsumption
       fields = ['amount']
