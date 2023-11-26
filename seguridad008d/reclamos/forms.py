from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django.forms import ModelForm
from .models import Reclamo

# LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = ReCaptchaField


class Create_Form(ModelForm):
    class Meta:
        model = Reclamo
        fields = ['asunto', 'cuerpo']