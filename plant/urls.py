from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('plant', views.plant_selection, name='plant'),
    path('plant-detail/<int:plant_id>/', views.plant_detail, name='plant_detail')
   
]
