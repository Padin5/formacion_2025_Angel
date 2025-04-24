"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25
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

<<<<<<< HEAD
## Importamos la interfaz de administración
from django.contrib import admin

## Importamos la creación de rutas
from django.urls import path

## Importamos la vista que queremos mostrar en el navegador
from main.views import index

## Esta lista tiene todas las rutas que acepta el sitio web. Django las recorre hasta encontrar una coincidencia
urlpatterns = [
    ## Al visitar admin, cargamos la interfaz de administración
    path("admin/", admin.site.urls),
    ## Ruta vacía a localhost, función que definimos en views, nombre identificador de la ruta
    path("", index, name="index"),
=======
from django.contrib import admin
from django.urls import path
from main.views import index, lines
from users.views import login_view, logout_view
from main.api import ExpenseViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="lista_gastos"),
    path(
        "api/gastos/",
        ExpenseViewSet.as_view({"get": "list", "post": "create"}),
        name="lista_gastos_api",
    ),
    path(
        "api/gastos/<int:pk>/",
        ExpenseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="gasto_api",
    ),
    path("lines/<int:expense>/", lines, name="lista_lineas_gasto"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25
]
