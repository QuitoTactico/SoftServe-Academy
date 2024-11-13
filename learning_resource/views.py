from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from user.models import User
from learning_route.models import LearningRouteResource
from .models import LearningResource
from .forms import LearningResourceForm, ReviewForm
from enums.enums import LANG_FLAG  # Import LANG_FLAG

def home(request):
    learning_resources = LearningResource.objects.all()
    return render(
        request, "learning_resource.html", {"learning_resources": learning_resources}
    )


@login_required
@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method == "POST":
        form = LearningResourceForm(request.POST)
        if form.is_valid():
            resource = form.save()  # Guardar el objeto y obtener la instancia
            resource.save()  # Llamar explícitamente al método save sobrescrito
            return redirect("learning_resource")
    else:
        form = LearningResourceForm()
        return render(request, "learning_resource_create.html", {"form": form})


# Second parameter is optional, to mark the resource as completed
@login_required
def detail(request, id: int, route_resource_id: int = None):
    try:
        learning_resource = LearningResource.objects.get(pk=id)

        if route_resource_id:
            route_resource = LearningRouteResource.objects.get(id=route_resource_id)
            route_resource.set_completed()
        else:
            route_resource = None

        review_form = ReviewForm()

        return render(
            request,
            "learning_resource_detail.html",
            {
                "learning_resource": learning_resource,
                "review_form": review_form,
                "lang_flag": LANG_FLAG,  # Add LANG_FLAG to context
                # ...existing context...
            },
        )
    except LearningResource.DoesNotExist:
        return redirect("not_found")


@login_required
def create_review(request, id: int):
    try:
        learning_resource = LearningResource.objects.get(pk=id)
        if request.method == "POST":
            form = ReviewForm(request.POST)
            if form.is_valid():
                previous_review = learning_resource.reviews.filter(
                    user=request.user
                ).first()

                review = form.save(commit=False)
                review.user = request.user

                if previous_review:
                    learning_resource.reviews.filter(user=request.user).delete()
                    if not review.comment.endswith(" (edited)"):
                        review.comment += " (edited)"

                review.save()
                learning_resource.reviews.add(review)
                return redirect("learning_resource_detail", id=id)
        else:
            form = ReviewForm()
        return redirect("learning_resource_detail", id=id)
    except LearningResource.DoesNotExist:
        return redirect("not_found")
