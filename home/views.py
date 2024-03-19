from django.http import HttpResponse
from django.template import loader
import requests

def home(request):
    url = "https://quotes15.p.rapidapi.com/quotes/random/"
    querystring = {"language_code": "pt"}

    headers = {
        "X-RapidAPI-Key": "c7dbb48416mshc7b606bd9ea37d5p142e70jsn559215ad5281",
        "X-RapidAPI-Host": "quotes15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    quote_data = response.json()

    template = loader.get_template("home.html")
    context = {
        'quote_data': quote_data
    }
    return HttpResponse(template.render(context, request))
