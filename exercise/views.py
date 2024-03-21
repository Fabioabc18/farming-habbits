from django.shortcuts import render, redirect
from .forms import DailyGoalsForm, ExerciseTypeForm


def set_daily_goals(request):
    if request.method == 'POST':
        form = DailyGoalsForm(request.POST)
        if form.is_valid():
            daily_goal = form.save(commit=False)
            daily_goal.user = request.user
            daily_goal.save()
            
    else:
        form = DailyGoalsForm()
    return render(request, 'set_daily_goals.html', {'form': form})

def select_exercise(request):
    if request.method == 'POST':
        form = ExerciseTypeForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            exercise.save()
            
    else:
        form = ExerciseTypeForm()
    return render(request, 'select_exercise.html', {'form': form})