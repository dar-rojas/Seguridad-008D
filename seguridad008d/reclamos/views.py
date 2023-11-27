from django.shortcuts import render, redirect
from .forms import Create_Form
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from reclamos.decorators import allowed_users, unauthenticaded_user
from axes.decorators import axes_dispatch
from reclamos.forms import LoginForm

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
        form = LoginForm()
        return render(request, 'login.html', {'form':form}) 
