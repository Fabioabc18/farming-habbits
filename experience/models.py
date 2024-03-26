from django.db import models
from django.contrib.auth import get_user_model



# --- XP ---

# classe para pontos de experiencia
class ExperiencePoints(models.Model):
   user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   points = models.PositiveIntegerField(default=0)
   level = models.IntegerField(default=1)








# --- Goals ---

# classe para criar Goals
class DailyGoals(models.Model):
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   date = models.DateField(auto_now_add=True)
   water_goal = models.PositiveIntegerField(default=0)
   exercise_time_goal = models.PositiveIntegerField(default=0) # exemplo: [tempo 10] * [tip.ex hard *3]
   calorie_goal = models.PositiveIntegerField(default=0)
   # Adicione outros campos de meta, se necessário

class ExerciseType(models.Model):
   exercise_type = models.CharField(max_length=100)
   exercise_difficulty = models.PositiveIntegerField(default=1)


