from django import forms
from .models import CaloriesConsumption

class CaloriesConsumptionForm(forms.ModelForm):
   class Meta:
       model = CaloriesConsumption
       fields = ['amount']
