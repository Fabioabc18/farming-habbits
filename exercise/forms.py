from django import forms
from experience.models import DailyGoals, ExerciseType

class DailyGoalsForm(forms.ModelForm):
    class Meta:
        model = DailyGoals
        fields = ['exercise_time_goal']

class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = ExerciseType
        fields = ['exercise_type']