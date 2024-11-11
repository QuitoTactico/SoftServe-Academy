from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def pricing(request):
    return render(request, "pricing.html")


def not_found(request):
    return render(request, "not_found.html")


def not_logged_in(request):
    return render(request, "not_logged_in.html")


def user_does_not_exist(request):
    return render(request, "user_does_not_exist.html")
