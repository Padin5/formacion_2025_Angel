from django.contrib import admin

from main.models import Expense

## Podemos modificar la interfaz del admin de nuestro localhost
class ExpenseAdmin(admin.ModelAdmin):
    ## Los fields son cabeceros de columna, para que no aparezca todo apelmazado
    fields = (
        "descripcion",
        "categoria",
        "limite",
    )
    ## Lo que nos aparece una vez introducimos una fila
    list_display = (
        "descripcion",
        "categoria",
        "limite",
        "fecha",
    )
    ## Filtrar por categoría
    list_filter = ("categoria", "limite")
    ## Buscador
    search_fields = ("categoria")
    ## Para ordenarlos
    ordering = ("limite")

admin.site.register(Expense)

