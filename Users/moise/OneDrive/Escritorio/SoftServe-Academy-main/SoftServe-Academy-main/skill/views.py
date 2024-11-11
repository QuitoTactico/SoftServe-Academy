from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Skill
from .forms import SkillForm


def home(request):
    skills = Skill.objects.all()
    return render(request, "skill.html", {"skills": skills})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method == "POST":
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("skill")
    else:
        form = SkillForm()
    return render(request, "skill_create.html", {"form": form})
