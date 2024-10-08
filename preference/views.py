from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.models import User
from .models import Preference
from .forms import PreferenceForm


@login_required
def create(request):
    if request.method == "POST":
        form = PreferenceForm(request.POST)
        if form.is_valid():
            preference = form.save(commit=False)
            user_id = request.session.get("user_id")
            if user_id:
                user = User.objects.get(id=user_id)
                preference.save()
                user.preference = preference
                user.save()
                return redirect("user")
        else:
            return render(request, "preference_create.html", {"form": form})
    else:
        form = PreferenceForm()
    return render(request, "preference_create.html", {"form": form})


def detail(request, id: int):
    # id es el id del usuario. por ahora no se usa.
    return render(request, "preference_detail.html")
