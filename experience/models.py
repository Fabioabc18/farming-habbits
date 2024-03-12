from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

# --- Goals ---

# classe para criar Goals
class DailyGoals(models.Model):
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   water_goal = models.PositiveIntegerField(default=0)
   exercise_goal = models.PositiveIntegerField(default=0)
   calorie_goal = models.PositiveIntegerField(default=0) # as calorias devia ser uma janela de valores!
   # Adicione outros campos de meta, se necessário

# --- XP ---

# classe para pontos de experiencia
class ExperiencePoints(models.Model):
   user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   points = models.PositiveIntegerField(default=0)

# --- Plant ---
  
# criar estagios da planta (1-5)
class Plant(models.Model):
   user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   experience = models.PositiveIntegerField(default=0)
   stage = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(5)])
