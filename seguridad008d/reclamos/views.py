from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from reclamos.decorators import allowed_users, unauthenticaded_user
from axes.decorators import axes_dispatch
from reclamos.forms import LoginForm

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
