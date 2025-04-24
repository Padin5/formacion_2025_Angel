## Con este archivo definimos un ViewSet, una clase especial de Django REST Framework para combinar operaciones CRUD

# Importamos todas las operaciones CRUD (los verbos list, create, destroy...)
from rest_framework import viewsets
# Reutilizamos la función de nuestro controller
from main.controller import get_expenses
# Necesitamos un serielizador para nuestra API para convertir objetos a JSON
from main.serializer import ExpenseSerializer
# Permisos para controlar quien accede a la API
from rest_framework import permissions


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = get_expenses()   # Qué datos manejamos
    serializer_class = ExpenseSerializer    # Como los serializamos
    permission_classes = [permissions.IsAuthenticated]  # Quien puede acceder a ellos