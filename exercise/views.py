from django.http import HttpResponse
from django.template import loader
from .forms import ExerciseDoneForm
from experience.models import ExperiencePoints
from experience.views import update_experience_points


def exercise_done(request):
    template = loader.get_template("exercise.html")

    if request.method == 'POST':
        form = ExerciseDoneForm(request.POST)
        if form.is_valid():
            exercise_done = form.save(commit=False)
            exercise_done.user = request.user
            exercise_done.save()

            update_experience_points(request.user, exercise_done.time)
            user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]

            context = {
                "form" : form,
                "user_experience": user_experience,
            }

            return HttpResponse ("registo com sucesso")
    else:
        form = ExerciseDoneForm()
        user_experience = ExperiencePoints.objects.get_or_create(user=request.user)[0]
        context = {
                "form" : form,
                "user_experience": user_experience,
            }
        return HttpResponse (template.render(context, request))
