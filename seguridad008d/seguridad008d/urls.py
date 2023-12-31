"""
URL configuration for seguridad008d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from reclamos.views import login_view, create_formulario, logout_view, reclamos_view, eliminar_reclamo

urlpatterns = [
    path('', create_formulario, name="formulario"),
    path('admin/', admin.site.urls),
    path('formulario/', create_formulario, name="formulario"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reclamos/', reclamos_view, name='reclamos'),
    path('eliminar_reclamo/<int:id>', eliminar_reclamo, name='eliminar_reclamo'),
]
