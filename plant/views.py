from django.shortcuts import render, redirect
from .forms import PlantSelectionForm
from .models import Plant, PlantProgress, UserCollection


def plant_selection(request):
    if request.method == 'POST':
        form = PlantSelectionForm(request.POST)
        if form.is_valid():
            plant_id = form.cleaned_data['plant']
            return redirect('plant_detail', plant_id=plant_id)
    else:
        form = PlantSelectionForm()
    
    context = {
            'form': form
        }
    return render(request, 'plant_selection.html', context)


def plant_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    progress, created = PlantProgress.objects.get_or_create(user=request.user, plant=plant)
    
    if request.method == 'POST':
        if progress.stage < plant.stages:
            # Update experience points for the plant
            progress.experience_points += 5  # Assuming 5 experience points for each action
            progress.save()

            # Check if the plant should level up
            if progress.experience_points >= 200 * progress.stage:
                progress.stage += 1
                progress.experience_points = 0  # Reset experience points for the next stage
                progress.save()
        
        return redirect('plant_selection')

    context = {
            'plant': plant, 'progress': progress
        }
    
    return render(request, 'plant_detail.html', context)


def collect_plant(request, plant_progress_id):
    plant_progress = PlantProgress.objects.get(id=plant_progress_id)

    # Add the fruit to the user's collection
    user_collection, created = UserCollection.objects.get_or_create(user=request.user)
    user_collection.fruits.add(plant_progress.plant)

    # Once the action is performed, you can reset the plant's progress or leave it unchanged
    # For example, you can reset the stage and experience points to 0:
    plant_progress.stage = 1
    plant_progress.experience_points = 0
    plant_progress.save()

    ### OR ##################################################################

    # Delete the progress entry
    plant_progress.delete()

    return redirect('plant_selection')
