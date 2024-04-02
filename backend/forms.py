from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)


class UploadExcelForm(forms.Form):
    file = forms.FileField()


#APIs


class FormularioUsuario(forms.Form):

    id_usuario = forms.IntegerField()
    user_name = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    sesion_activa = forms.BooleanField()
