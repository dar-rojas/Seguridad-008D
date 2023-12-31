from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django.forms import ModelForm
from .models import Reclamo

# LOGIN
class LoginForm(forms.Form):
    username = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    captcha = ReCaptchaField()


class Create_Form(ModelForm):
    captcha = ReCaptchaField()
    asunto = forms.CharField(max_length = 150, widget=forms.TextInput(attrs={'class':'form-control'}))
    cuerpo = forms.CharField(max_length = 1000, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Reclamo
        fields = ('asunto', 'cuerpo', 'captcha')