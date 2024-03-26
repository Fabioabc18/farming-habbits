from django import forms
from .models import ExerciseDone


class ExerciseDoneForm(forms.ModelForm):
   class Meta:
       model = ExerciseDone
       fields = ['time']
