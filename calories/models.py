from django.db import models
from django.contrib.auth import get_user_model


class CaloriesConsumption(models.Model):
   user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
   amount = models.FloatField()  # Quantidade de calorias consumidas
   date = models.DateField(auto_now_add=True)  # Data em que foram consumidas
