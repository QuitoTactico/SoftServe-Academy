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
from django.urls import path
from home import views as homeViews
from user import views as userViews
from learning_route import views as learningRouteViews
from learning_resource import views as learningResourceViews

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', homeViews.home, name='home'),
    path('about/', homeViews.about, name='about'),
    path('contact/', homeViews.contact, name='contact'),

    # User
    path('login/', userViews.login, name='login'),
    path('logout/', userViews.logout, name='logout'),
    path('register/', userViews.register, name='register'),

    # Learning Route
    path('learning_route/', learningRouteViews.home, name='learning_route_list'),
    path('learning_route/<int:id>/', learningRouteViews.detail, name='learning_route_detail'),

    # Learning Resource
    path('learning_resource/', learningResourceViews.home, name='learning_resource_list'),
    path('learning_resource/create/', learningResourceViews.create, name='learning_resource_create'), # por ahora será el sqlite admin
    path('learning_resource/<int:id>/', learningResourceViews.detail, name='learning_resource_detail'),
]
