from django.shortcuts import render, redirect
from .models import WaterConsumption
from .forms import WaterConsumptionForm
from experience.models import ExperiencePoints, Plant, DailyGoals
from experience.views import update_experience_points


def water_consumption(request):
   if request.method == 'POST':
       form = WaterConsumptionForm(request.POST)
       if form.is_valid():
           water_consumption = form.save(commit=False)
           water_consumption.user = request.user
           water_consumption.save()
           update_daily_goals(request, water_consumption.amount)
           # Suponha que o usuário ganhe 10 pontos de experiência por cada 100 ml de água consumida
           points_gained = int(water_consumption.amount / 100) * 10
           update_experience_points(request, points_gained)
           return redirect('water_consumption')
   else:
       form = WaterConsumptionForm()

   # isto pode ser util, nao apagar para já :)
    # update_experience_points(request, points_gained)
    # update_plant_stage(request)

   water_data = WaterConsumption.objects.filter(user=request.user)
   return render(request, 'water_tracker/water_consumption.html', {'form': form, 'water_data': water_data})


def update_daily_goals(request, amount_consumed):
   user_daily_goals, created = DailyGoals.objects.get_or_create(user=request.user)
   # Atualiza os objetivos diários de água conforme necessário
   user_daily_goals.water_goal += amount_consumed
   user_daily_goals.save()
