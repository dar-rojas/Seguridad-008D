from django.shortcuts import render, redirect, get_object_or_404
from .forms import Create_Form
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from reclamos.decorators import allowed_users, unauthenticaded_user
from axes.decorators import axes_dispatch
from reclamos.forms import LoginForm
from reclamos.models import Reclamo
from django.http import HttpResponseNotAllowed

@allowed_users(allowed_roles=['Cliente'])
def create_formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html', {'form': Create_Form})
    else:
        try:
            form = Create_Form(request.POST)
            if not form.is_valid():
                messages.error(request, ("Complete todos los campos correctamente para continuar"))
                return redirect('formulario')
            
            new_form = form.save(commit=False)
            
            # Establecer el valor de estado en 1
            new_form.estado = 1
            new_form.usuario = request.user
            new_form.save()

            messages.success(request, ("Muchas gracias, su reclamo será revisado por nuestro personal"))
            return redirect(reverse('formulario'))
        except ValueError:
            return render(request, 'formulario.html', {
                'form': Create_Form,
                'error': 'Introduzca datos válidos'
            })

#LOGIN
@axes_dispatch
@unauthenticaded_user
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('formulario')
            else:
                messages.error(request, ("Usuario o contraseña inválida"))
                return redirect('login')
        else:
            messages.error(request, ("Captcha necesario para continuar"))
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form}) 

#LOGOUT
@allowed_users(allowed_roles=['Cliente', 'Admin'])
def logout_view(request):
    logout(request)
    messages.success(request, ("Sesión cerrada exitosamente"))
    return redirect('login')

#RECLAMOS
@allowed_users(allowed_roles=['Admin'])
def reclamos_view(request):
    if request.method == 'GET':
        reclamos = Reclamo.objects.all().filter(
            estado=1
        )
        datos = {'reclamos' : reclamos}
        return render(request, 'reclamos.html', datos)
    else:
        return HttpResponseNotAllowed(['GET'])

#ELIMINAR RECLAMO
@allowed_users(allowed_roles=['Admin'])
def eliminar_reclamo(request, id):
    reclamo = get_object_or_404(Reclamo, pk=id)
    reclamo.estado = 0
    reclamo.save()
    return redirect('reclamos')