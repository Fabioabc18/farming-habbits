from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import WaterConsumptionForm
from experience.models import DailyGoals, ExperiencePoints
from experience.views import update_experience_points


def water_consumption(request):
    template = loader.get_template("water.html")

    if request.method == 'POST':
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water_consumption = form.save(commit=False)
            water_consumption.user = request.user
            water_consumption.save()

            update_experience_points(request.user, water_consumption.amount)
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]

            context = {
                "form" : form,
                "user_experience": user_experience,
            }

            return HttpResponse ("registo com sucesso")
    else:
        form = WaterConsumptionForm()
        user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
        context = {
                "form" : form,
                "user_experience": user_experience,
            }
        return HttpResponse (template.render(context, request))





def update_daily_goals(request, amount_consumed):
    user_daily_goals, created = DailyGoals.objects.get_or_create(user=request.user)
    # Atualiza os objetivos diários de água conforme necessário
    user_daily_goals.water_goal += amount_consumed
    user_daily_goals.save()

