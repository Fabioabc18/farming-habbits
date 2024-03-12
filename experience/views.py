from django.shortcuts import redirect
from .models import ExperiencePoints, Plant


# --- XP ---

def update_experience_points(request, points):
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)
   user_experience.points += points
   user_experience.save()

# --- Plant ---

def update_plant_growth(request):
   user_plant, created = Plant.objects.get_or_create(user=request.user)
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)
  
   # Lógica para atualizar o crescimento da planta com base nos pontos de experiência do usuário
   while user_plant.stage < 5 and user_experience.points >= user_plant.stage * 300:
       user_experience.points -= user_plant.stage * 300
       user_plant.stage += 1
       user_plant.save()
       user_experience.save()

def collect_plant(request):
   user_plant, created = Plant.objects.get_or_create(user=request.user)
   user_experience, created = ExperiencePoints.objects.get_or_create(user=request.user)

   # Se a planta estiver no estágio final, reinicie o crescimento da planta e os pontos de experiência do usuário
   if user_plant.stage == 5:
       user_plant.stage = 1
       # user_plant.experience = 0
       user_experience.points = 0
       user_plant.save()
       user_experience.save()
