from django.forms import ModelForm
from .models import Reclamo

class Create_Form(ModelForm):
    class Meta:
        model = Reclamo
        fields = ['fecha', 'asunto', 'cuerpo', 'estado']