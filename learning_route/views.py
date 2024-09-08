from django.shortcuts import render, redirect, get_object_or_404
from .models import LearningRoute
from user.models import User

def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = get_object_or_404(User, id=user_id)
            resources = user.learning_routes.all()  # Obtener los recursos de aprendizaje del usuario
        except:
            return redirect('user_does_not_exist')
    else:
        resources = LearningRoute.objects.none()  # No hay usuario en la sesión, devolver un queryset vacío
        return redirect('not_logged_in')
    
    return render(request, 'user.html', 
                  {'resources': resources})


def detail(request, id: int):
    # id es el id de la ruta específica. por ahora no se usa.
    return render(request, 'learning_route_detail.html')
