from django.shortcuts import redirect
from .models import ExperiencePoints, Plant
from .forms import PlantForm


# --- XP ---

def update_experience_points(request, points):
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)
   user_experience.points += points
   user_experience.save()
   update_plant_growth(request)

# --- Plant ---


def update_plant_growth(request):
   # ARRANJAR UM ID DE TIPO DE PLANTA
   user_plant, created = Plant.objects.get_or_create(user=request.user)
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)
  
   # Lógica para atualizar o crescimento da planta com base nos pontos de experiência do usuário
   if user_plant.stage < 5 and user_experience.points >= user_plant.stage * 300:
       user_experience.points -= user_plant.stage * 300
       user_plant.stage += 1
       user_plant.save()
       user_experience.save()


def collect_plant(request):
   user_plant, created = Plant.objects.get_or_create(user=request.user)
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)

   # Se a planta estiver no estágio final, reinicie o crescimento da planta e os pontos de experiência do usuário
   if user_plant.stage == 5:
       user_plant.stage = 0
       user_plant.experience = 0
       user_experience.points = 0
       user_plant.save()
       user_experience.save()


def reset_plant_type_after_collect(request):
   user_plant, created = Plant.objects.get_or_create(user=request.user)
   plant_type, created = Plant.objects.get_or_create(user=request.user)

   if user_plant.stage == 0:
      plant_type.type = ""
   # se o type for vazio "", n aparece imagem 
   # chamar o botao de "select_plant_basic"


def select_plant_basic(request):
    if request.method == 'POST':
        form = PlantForm(request.POST)
        if form.is_valid():
            plant_type = form.save(commit=False)
            plant_type.user = request.user
            plant_type.save()
            update_plant_growth(request)
    else:
        form = PlantForm()


