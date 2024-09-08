from django.shortcuts import render, redirect
from .models import LearningResource
from .forms import LearningResourceForm

def home(request):
    learning_resources = LearningResource.objects.all()
    return render(request, 'learning_resource.html', 
                  {'learning_resources': learning_resources})

def create(request):
    if request.method == 'POST':
        form = LearningResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'learning_resource.html', 
                          {'success': True}) # Redirige a una URL de éxito
    else:
        form = LearningResourceForm()
        return render(request, 'learning_resource_create.html', 
                    {'form': form})

def detail(request, id: int):
    try:
        learning_resource = LearningResource.objects.get(pk=id)
        return render(request, 'learning_resource_detail.html',
                    {'learning_resource': learning_resource})
    except LearningResource.DoesNotExist:
        return redirect('not_found')