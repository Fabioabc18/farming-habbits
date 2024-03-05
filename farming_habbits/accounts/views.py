from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    template = loader.get_template("registration/register.html")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        username = request.POST.get("username")
        email = request.POST.get("email")
        contacto = request.POST.get("contacto")
        

        try:
            if form.is_valid() and form["password1"].value() == form["password2"].value():
                user = User.objects.create_user(username=username, password=form["password1"].value(), email=email, contacto = contacto)
                user.save()
                return redirect("/")
            else:
                context = {
                    "form": form,
                    "message": "Passwords diferentes!"
                }
                return HttpResponse(template.render(context, request))

        except:
            context = {
                "form": form,
                "message": "Ocorreu um erro!"
            }
            return HttpResponse(template.render(context, request))

    else:
        form = UserCreationForm()

        context = {
            "form": form
        }
        return HttpResponse(template.render(context, request))
