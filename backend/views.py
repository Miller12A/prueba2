from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Usuario
from backend.models import Usuario
from .forms import UploadExcelForm
import pandas as pd
from backend.forms import FormularioUsuario

# Create your views here.


def mantenimiento(request):
    return render(request, 'mantenimiento_usuario.html')

def bienvenida(request):
    return render(request, 'bienvenida.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'inicio.html')

def usuarios(request):
    return render(request, 'usuarios.html')


def lista_usuarios(request):
    usuarios = Usuario.objects.all() 
    return render(request, 'usuarios.html', {'usuarios': usuarios})


    
def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos.')
    return render(request, 'login.html')


def upload_excel(request):
    if request.method == 'POST':
        form = UploadExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES['file']
            if excel_file.name.endswith('.xlsx'):
                try:
                    df = pd.read_excel(excel_file)
                    for index, row in df.iterrows():
                        usuario = Usuario(
                            id_usuario=row['id'],
                            user_name=row['user_name'],
                            password=row['password'],
                            email=row['email'],
                            sesion_activa=row['sesion_activa']
                        )
                        usuario.save()
                    return HttpResponse('Carga masiva exitosa')
                except Exception as e:
                    return render(request, 'upload_excel.html', {'form': form, 'error_message': 'No se pudo guardar el archivo en la base de datos.'})
            else:
                return HttpResponse('El archivo no es un archivo Excel válido o no cumple con los Requisitos')
    else:
        form = UploadExcelForm()
    return render(request, 'upload_excel.html', {'form': form})


def createUSer(request):
    if request.method=="POST":
        miFormulario = FormularioUsuario(request.POST)

        if miFormulario.is_valid():
            infForm = miFormulario.cleaned_data

            return render(request, "usuarios.html")
        
    else:
        miFormulario = FormularioUsuario()

    return render(request, "crear_usuarios.html", {"form":miFormulario})