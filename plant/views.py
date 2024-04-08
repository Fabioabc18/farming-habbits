from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import PlantSelectionForm
from .models import Plant, PlantProgress
from django.template import loader

def plant_selection(request):
    if request.method == 'POST':
        form = PlantSelectionForm(request.POST)
        if form.is_valid():
            plant = form.cleaned_data['plant']
            return redirect('plant_detail', plant_id=plant.id)
    else:
        form = PlantSelectionForm()

    context = {'form': form}
    template = loader.get_template('plant.html')
    return HttpResponse(template.render(context, request))

def plant_detail(request, plant_id):
   
    plant = Plant.objects.get(id=plant_id)
    
    progress, _ = PlantProgress.objects.get_or_create(user=request.user, plant=plant)

    
    context = {
        'plant': plant,
        'progress': progress
    }

    
    template = loader.get_template('plant_detail.html')

    
    rendered_template = template.render(context, request)

   
    return HttpResponse(rendered_template)