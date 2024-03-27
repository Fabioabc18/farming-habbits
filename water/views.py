from django.http import HttpResponse
from django.template import loader
from .forms import WaterConsumptionForm
from experience.models import ExperiencePoints
from .models import WaterConsumption
from experience.views import update_experience_points

def water_consumption(request):
    template = loader.get_template("water.html")

    if request.method == 'POST':
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            water_consumption = form.save(commit=False)
            water_consumption.user = request.user
            water_consumption.save()

            update_experience_points(request.user, water_consumption.amount*2)
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
            historico = WaterConsumption.objects.filter(user=request.user).order_by('-date')[:10]

            context = {
                "form" : form,
                "user_experience": user_experience,
                "error_message": None,
                'username': request.user.username,
                'historico' : historico
            }

            return HttpResponse("Registro com sucesso")
        else:
            # Se o formulário não for válido, renderize o template novamente com o formulário e uma mensagem de erro
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
            historico = WaterConsumption.objects.filter(user=request.user).order_by('-date')[:10]

            context = {
                "form" : form,
                "user_experience": user_experience,
                'username': request.user.username,
                'historico' : historico,
                "error_message": "Por favor, insira um valor válido para o consumo de água."
            }
            return HttpResponse(template.render(context, request))

    else:
        form = WaterConsumptionForm()
        user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
        historico = WaterConsumption.objects.filter(user=request.user).order_by('-date')[:10]

        context = {
            "form" : form,
            "user_experience": user_experience,
            'username': request.user.username,
            "error_message": None,
            'historico' : historico
        }
        return HttpResponse(template.render(context, request))


def update_daily_goals(request, amount_consumed):
    user_daily_goals, created = DailyGoals.objects.get_or_create(user=request.user)
    user_daily_goals.water_goal += amount_consumed
    user_daily_goals.save()
