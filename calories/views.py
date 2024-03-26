from django.http import HttpResponse
from django.template import loader
from .forms import CaloriesConsumptionForm
from experience.models import ExperiencePoints
from experience.views import update_experience_points


def calories_consumption(request):
    template = loader.get_template("calories.html")

    if request.method == 'POST':
        form = CaloriesConsumptionForm(request.POST)
        if form.is_valid():
            calories_consumption = form.save(commit=False)
            calories_consumption.user = request.user
            calories_consumption.save()

            update_experience_points(request.user, calories_consumption.amount)
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]

            context = {
                "form" : form,
                "user_experience": user_experience,
            }

            return HttpResponse ("registo com sucesso")
    else:
        form = CaloriesConsumptionForm()
        user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
        context = {
                "form" : form,
                "user_experience": user_experience,
            }
        return HttpResponse (template.render(context, request))
