from django.urls import path
from . import views

urlpatterns = [
    path("exercise",views.exercise_done, name="exercise"),  
    
]
