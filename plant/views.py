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
    # Obtenha a planta com base no ID fornecido
    plant = Plant.objects.get(id=plant_id)
    # Obtenha o progresso da planta para o usuário atual
    progress, _ = PlantProgress.objects.get_or_create(user=request.user, plant=plant)

    # Construa o contexto com os dados da planta e do progresso
    context = {
        'plant': plant,
        'progress': progress
    }

    # Carregue o template
    template = loader.get_template('plant_detail.html')

    # Renderize o template com o contexto
    rendered_template = template.render(context, request)

    # Retorne a resposta HTTP com o template renderizado
    return HttpResponse(rendered_template)