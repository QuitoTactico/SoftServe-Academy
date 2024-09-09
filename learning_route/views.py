from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LearningRoute
from user.models import User

@login_required
def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = get_object_or_404(User, id=user_id)
            learning_routes = user.learning_routes.all()  # Obtener los recursos de aprendizaje del usuario
        except:
            return redirect('user_does_not_exist')
    else:
        learning_routes = LearningRoute.objects.none()  # No hay usuario en la sesión, devolver un queryset vacío
        return redirect('not_logged_in')
    
    return render(request, 'learning_route.html', 
                  {'learning_routes': learning_routes})


def detail(request, id: int):
    # id es el id de la ruta específica. por ahora no se usa.
    return render(request, 'learning_route_detail.html')
