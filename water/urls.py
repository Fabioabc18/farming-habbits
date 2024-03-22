from django.urls import path
from . import views

urlpatterns = [
    path("water",views.water_consumption, name="water"),  
    
]
