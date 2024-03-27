from django.http import HttpResponse
from django.template import loader
from .forms import CaloriesConsumptionForm
from experience.models import ExperiencePoints
from .models import CaloriesConsumption
from experience.views import update_experience_points
from home.views import get_quote

def calories_consumption(request):
    template = loader.get_template("calories.html")

    if request.method == 'POST':
        form = CaloriesConsumptionForm(request.POST)
        if form.is_valid():
            calories_consumption = form.save(commit=False)
            calories_consumption.user = request.user
            calories_consumption.save()

            update_experience_points(request.user, calories_consumption.amount*2)
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
            historico = CaloriesConsumption.objects.filter(user=request.user).order_by('-date')[:10]

            quote_data = get_quote()
            
            context = {
                "form" : form,
                'quote_data': quote_data,
                "user_experience": user_experience,
                'username': request.user.username,
                "error_message": None,
                'historico' : historico
            }

            return HttpResponse ("registo com sucesso")
        else:
            # Se o formulário não for válido, renderize o template novamente com o formulário e uma mensagem de erro
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
            historico = CaloriesConsumption.objects.filter(user=request.user).order_by('-date')[:10]

            quote_data = get_quote()
            
            context = {
                "form" : form,
                'quote_data': quote_data,
                "user_experience": user_experience,
                'username': request.user.username,
                'historico' : historico,
                "error_message": "Por favor, insira um valor válido para o consumo de água."
            }
            return HttpResponse(template.render(context, request))
        
    else:
        form = CaloriesConsumptionForm()
        user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
        historico = CaloriesConsumption.objects.filter(user=request.user).order_by('-date')[:10]

        quote_data = get_quote()
        
        context = {
                "form" : form,
                'quote_data': quote_data,
                "user_experience": user_experience,
                'username': request.user.username,
                "error_message": None,
                'historico' : historico
            }
        return HttpResponse (template.render(context, request))
