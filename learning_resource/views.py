from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from learning_route.models import LearningRouteResource
from .models import LearningResource
from .forms import LearningResourceForm

def home(request):
    learning_resources = LearningResource.objects.all()
    return render(request, 'learning_resource.html', 
                  {'learning_resources': learning_resources})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method == 'POST':
        form = LearningResourceForm(request.POST)
        if form.is_valid():
            resource = form.save()  # Guardar el objeto y obtener la instancia
            resource.save()  # Llamar explícitamente al método save sobrescrito
            return redirect('learning_resource')
    else:
        form = LearningResourceForm()
        return render(request, 'learning_resource_create.html', 
                    {'form': form})

# Second parameter is optional, to mark the resource as completed
def detail(request, id: int, route_resource_id: int = None):
    try:
        learning_resource = LearningResource.objects.get(pk=id)
        
        if route_resource_id:
            route_resource = LearningRouteResource.objects.get(id=route_resource_id)
            route_resource.set_completed()
        else:
            route_resource = None

        return render(request, 'learning_resource_detail.html',
                    {'learning_resource': learning_resource})
    except LearningResource.DoesNotExist:
        return redirect('not_found')
    
