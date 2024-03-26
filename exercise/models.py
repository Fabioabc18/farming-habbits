from django.db import models
from django.contrib.auth import get_user_model


class ExerciseDone(models.Model):
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   time = models.FloatField()  # Quantidade de tempo de exercício
   date = models.DateField(auto_now_add=True)  # Data em que foi submetido
