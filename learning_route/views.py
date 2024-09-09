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

@login_required
def detail(request, id: int):
    user_id = request.session.get('user_id')
    if user_id:
        user = get_object_or_404(User, id=user_id)
        learning_route = user.learning_routes.filter(id=id).first()
        if not learning_route:
            return redirect('not_found')
    else:
        return redirect('not_logged_in')

    learning_route_resources = learning_route.learning_route_resources.all()
    target_skill_level = learning_route.skill_level.level

    ''' # Horrific
    learning_resources_by_level = []
    for i in range(1, target_skill_level + 1):
        resources_actual_level = learning_route_resources.filter(
            learning_resource__learning_skills__skill__name=target_skill_name,
            learning_resource__learning_skills__level=i)
        
        if resources_actual_level:
            learning_resources_by_level.append(
                {'level': i,
                 'resources': resources_actual_level})
            
    print(learning_resources_by_level)
    '''

    learning_resources_by_level = []
    for i in range(1, target_skill_level + 1):
        resources_actual_level = learning_route_resources.filter(level=i).order_by('index')
        
        if resources_actual_level:
            learning_resources_by_level.append(
                {'level': i,
                 'resources': resources_actual_level})

    return render(request, 'learning_route_detail.html',
                  {'learning_route': learning_route,
                   'learning_route_resources_by_level': learning_resources_by_level
                   })
