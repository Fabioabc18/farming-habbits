from .models import ExperiencePoints
from plant.models import PlantProgress


# --- XP ---

def update_experience_points(user, new_points):
   user_experience, _ = ExperiencePoints.objects.get_or_create(user=user)
   user_experience.points += new_points
   user_experience.save()

   level_threshold = 300  # XP threshold for each level
   user_experience.level = (user_experience.points // level_threshold) + 1
   user_experience.save()


   user_plants = PlantProgress.objects.filter(user=user)
   
   
   for plant in user_plants:
        plant.experience_points += new_points
        if plant.experience_points >= 200 * plant.stage:
            plant.experience_points -= 200 * plant.stage
            plant.stage += 1
            plant.save()
