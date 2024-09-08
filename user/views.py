from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm, LoginForm
from .models import User

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = get_object_or_404(User, id=user_id)
            return render(request, 'user.html', {'user': user}) # Happy path
        except:
            return redirect('user_does_not_exist')
    else:
        return redirect('not_logged_in')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['user_id'] = user.id  # Save the user id in the session
                return redirect('user')  # Happy path
            else:
                # Auth error
                return render(request, 'user_login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'form': form})


# It sends you to the login too, but deleting the session
def logout(request):
    auth_logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            auth_login(request, user)
            request.session['user_id'] = user.id
            return redirect('user')
        else:
            return render(request, 'user_register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'user_register.html', {'form': form})