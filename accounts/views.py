from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    template = loader.get_template("registration/register.html")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            if password1 == password2:
                try:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    messages.success(request, "Conta criada com sucesso. Faça login agora!")
                    return redirect("login")  
                except Exception as e:
                    context = {
                        "form": form,
                        "message": f"Ocorreu um erro: {str(e)}"
                    }
                    return HttpResponse(template.render(context, request))
            else:
                context = {
                    "form": form,
                    "message": "As senhas não coincidem."
                }
                return HttpResponse(template.render(context, request))
        else:
            context = {
                "form": form,
                "message": "Por favor, corrija os erros no formulário."
            }
            return HttpResponse(template.render(context, request))

    else:
        form = RegistrationForm()

        context = {
            "form": form,
            
        }
        return HttpResponse(template.render(context, request))