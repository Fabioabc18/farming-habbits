from django.urls import path
from . import views

urlpatterns = [
    path('plant/', views.plant_selection, name='plant'),
    path('plant_detail/<int:plant_id>/', views.plant_detail, name='plant_detail')
]
