from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import (
    RegisterForm,
    LoginForm,
    CurrentSkillsForm,
    TargetSkillsForm,
    ProfileUpdateForm,
)
from .models import User


@login_required
def home(request):
    user_id = request.session.get("user_id")
    if user_id:
        user = get_object_or_404(User, id=user_id)
        return render(request, "user.html", {"user": user})  # Happy path
    else:
        return redirect(
            "not_logged_in"
        )  # Not necessary now, because of the login_required decorator


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                request.session["user_id"] = user.id  # Save the user id in the session
                return redirect("user")  # Happy path
            else:
                # Auth error
                return render(
                    request,
                    "user_login.html",
                    {"form": form, "error": "Invalid credentials"},
                )
    else:
        form = LoginForm()
    return render(request, "user_login.html", {"form": form})


# It sends you to the login too, but deleting the session
def logout(request):
    auth_logout(request)
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            auth_login(request, user)
            request.session["user_id"] = user.id
            return redirect("user")
        else:
            return render(request, "user_register.html", {"form": form})
    else:
        form = RegisterForm()
    return render(request, "user_register.html", {"form": form})


@login_required
def update_current_skills(request):
    if request.method == "POST":
        form = CurrentSkillsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            session_user = User.objects.get(id=request.session["user_id"])
            session_user.save()
            return redirect("user")
    else:
        form = CurrentSkillsForm(instance=request.user)
    return render(request, "update_current_skills.html", {"form": form})


@login_required
def update_target_skills(request):
    if request.method == "POST":
        form = TargetSkillsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            session_user = User.objects.get(id=request.session["user_id"])
            session_user.save()
            return redirect("user")
    else:
        form = TargetSkillsForm(instance=request.user)
    return render(request, "update_target_skills.html", {"form": form})


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("user")
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, "update_profile.html", {"form": form, "user": request.user})
