"""
URL configuration for onlyflans_jp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from web.views import index, about, welcome # Importa las vistas de la  app "web"

urlpatterns = [
    path('admin/', admin.site.urls),  # ruta del administrador de Django
    path('', index, name='index'),  # ruta para la página de inicio
    path('acerca/', about, name='about'),  # ruta para la página acerca
    path('bienvenido/', welcome, name='welcome'),  # ruta para la página de bienvenida
]
