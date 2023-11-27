from django.shortcuts import redirect
from django.contrib.auth import logout

#funcion para usuario no autenticado
def unauthenticaded_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            #Agregar redireccion al anadir mas paginas
            if not request.user.groups.exists():
                logout(request) # si no pertenece a ningun grupo se deslogea y redirige a login
                return redirect('login')   
            group = request.user.groups.all()[0].name
            if group == 'Cliente':
                return redirect('formulario') #si esta autenticado lo redirige a los reclamos    
            if group == 'Admin':
                return redirect('reclamos')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

#funcion para diferenciar acceso por tipo de usuario
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                #obtiene el grupo al que pertenece el usuario
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper_func
    return decorator