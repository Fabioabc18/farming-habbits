from django.http import HttpResponse
from django.template import loader
from experience.models import ExperiencePoints
from django.contrib.auth.decorators import login_required
import requests

@login_required
def home(request):

    quote_data = get_quote()
    user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
    template = loader.get_template("home.html")
    context = {
        'quote_data': quote_data,
        'username': request.user.username,
        'user_experience': user_experience,
        
    }
    return HttpResponse(template.render(context, request))


def get_quote():
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code": "pt"}

    headers = {
        "X-RapidAPI-Key": "c7dbb48416mshc7b606bd9ea37d5p142e70jsn559215ad5281",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()