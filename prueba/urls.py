"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from backend import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.iniciar_sesion, name='login'),
    path('home/', views.home), 
    path('upload_excel/', views.upload_excel, name='upload_excel'),
    path('bienvenida/', views.bienvenida, name='bienvenida'),
    path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('usuarios/', views.lista_usuarios, name='usuarios'),
    path('create_user/', views.createUSer),
]
