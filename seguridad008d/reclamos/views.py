from django.shortcuts import render
from .forms import Create_Form

# Create your views here.
def create_formulario(request):
    return render(request, 'formulario.html', { 'form': Create_Form})