from .models import ExperiencePoints
from plant.models import Plant


# --- XP ---

def update_experience_points(user, new_points):
   user_experience, _ = ExperiencePoints.objects.get_or_create(user=user)
   user_experience.points += new_points
   user_experience.save()

   level_threshold = 300  # XP threshold for each level
   user_experience.level = (user_experience.points // level_threshold) + 1
   user_experience.save()

