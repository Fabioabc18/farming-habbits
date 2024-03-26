from django.db import models
from django.contrib.auth.models import User


class Plant(models.Model):
    name = models.CharField(max_length=100)
    

class PlantProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    stage = models.IntegerField(default=1)  # Current growth stage of the plant
    experience_points = models.IntegerField(default=0)  # Experience points for the plant

    
class UserCollection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fruits = models.ManyToManyField(Plant)  # Assuming each fruit is a plant