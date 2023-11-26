from django.shortcuts import render, redirect
from .forms import Create_Form
from django.urls import reverse

# Create your views here.
def create_formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html', {'form': Create_Form})
    else:
        try:
            form = Create_Form(request.POST)
            new_form = form.save(commit=False)
            
            # Establecer el valor de estado en 1
            new_form.estado = 1

            # Asignar el usuario actual (si estás utilizando el sistema de autenticación de Django)
            if request.user.is_authenticated:
                new_form.usuario = request.user

            new_form.save()

            return redirect(reverse('formulario'))
        except ValueError:
            return render(request, 'formulario.html', {
                'form': Create_Form,
                'error': 'Introduzca datos válidos'
            })