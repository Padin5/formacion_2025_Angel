"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

## Importamos la interfaz de administración
from django.contrib import admin

## Importamos la creación de rutas
from django.urls import path

## Importamos la vista que queremos mostrar en el navegador
from main.views import index

# Importamos del archivo api la clase ViewSet
from main.api import ExpenseViewSet

## Esta lista tiene todas las rutas que acepta el sitio web. Django las recorre hasta encontrar una coincidencia
urlpatterns = [
    ## Al visitar admin, cargamos la interfaz de administración
    path("admin/", admin.site.urls),
    ## Ruta vacía a localhost, función que definimos en views, nombre identificador de la ruta
    path("", index, name="index"),

    ## Definimos los métodos permitidos tanto en peticion get como post
    path("api/gastos/", ExpenseViewSet.as_view({"get": "list", "post": "create"}), name="lista_gastos_api",),
    # Definimos nuevamente los métodos permitidos en casa tipo de petición
    path("api/gastos/<int:pk>/", ExpenseViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),name="gasto_api",),
]
