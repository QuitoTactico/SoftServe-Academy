from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
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
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['user_id'] = user.id  # Guardar el ID del usuario en la sesión
            return redirect('home')
        else:
            # Manejar error de autenticación
            return render(request, 'user_login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'user_login.html')

def logout(request):
    return render(request, 'user_logout.html')

def register(request):
    return render(request, 'user_register.html')