"""
URL configuration for SoftServeAcademy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from home import views as homeViews
from user import views as userViews
from preference import views as preferenceViews
from learning_route import views as learningRouteViews
from learning_resource import views as learningResourceViews
from skill import views as skillViews

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    # Include Grappelli URL configuration
    path("admin/", admin.site.urls),
    # Anything not marked as MVP will be handled from the Django admin or is not essential
    # When using href={{ url 'name' }} in templates, use the name parameter specified here as the third argument
    # Please use the form {{ url 'learning_resource_create' }} instead of raw string URLs like "/learning_resource/create"
    # Home
    path("", homeViews.home, name="home"),
    path("about/", homeViews.about, name="about"),
    path("pricing/", homeViews.pricing, name="pricing"),
    # Errors. They are in home because every app can be redirected to this.
    path("not_found/", homeViews.not_found, name="not_found"),
    path("not_logged_in/", homeViews.not_logged_in, name="not_logged_in"),
    path(
        "user_does_not_exist/",
        homeViews.user_does_not_exist,
        name="user_does_not_exist",
    ),
    # User
    path("user/", userViews.home, name="user"),  # MVP
    path("login/", userViews.login, name="login"),
    path("logout/", userViews.logout, name="logout"),
    path("register/", userViews.register, name="register"),  # MVP
    path(
        "user/update_current_skills/",
        userViews.update_current_skills,
        name="update_current_skills",
    ),
    path(
        "user/update_target_skills/",
        userViews.update_target_skills,
        name="update_target_skills",
    ),
    path("user/update_profile/", userViews.update_profile, name="update_profile"),
    # Preferences
    path(
        "preference/create/", preferenceViews.create, name="preference_create"
    ),  # MVP!!!
    path(
        "preference/<int:id>/", preferenceViews.detail, name="preference_detail"
    ),  # MVP
    # Learning Route
    path("learning_route/", learningRouteViews.home, name="learning_route"),  # MVP
    path(
        "learning_route/generate/",
        learningRouteViews.generate,
        name="learning_route_generate",
    ),  # MVP!!!
    path(
        "learning_route/update/<int:id>/",
        learningRouteViews.update,
        name="learning_route_update",
    ),
    path(
        "learning_route/<int:id>/",
        learningRouteViews.detail,
        name="learning_route_detail",
    ),  # MVP!!!
    # Learning Resource
    path("learning_resource/", learningResourceViews.home, name="learning_resource"),
    path(
        "learning_resource/create/",
        learningResourceViews.create,
        name="learning_resource_create",
    ),
    path(
        "learning_resource/<int:id>/",
        learningResourceViews.detail,
        name="learning_resource_detail",
    ),  # MVP!!!
    path(
        "learning_resource/<int:id>/create_review/",
        learningResourceViews.create_review,
        name="learning_resource_create_review",
    ),
    path(
        "learning_resource/<int:id>/<int:route_resource_id>/",
        learningResourceViews.detail,
        name="learning_resource_detail",
    ),  # MVP!!!
    # Skill
    path("skill/", skillViews.home, name="skill"),
    path("skill/create/", skillViews.create, name="skill_create"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
