from django.urls import path
from . import views

urlpatterns = [
    path("calories",views.calories_consumption, name="calories"),  
   
]
