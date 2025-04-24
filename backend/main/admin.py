<<<<<<< HEAD
## Importamos el modulo de Django para gestionar la interfaz de administración
from django.contrib import admin

## Importamos el modelo creado previamente
from main.models import Expense

## Con esta clase podemos modificar la interfaz del admin. Hereda de admin.ModelAdmin
class ExpenseAdmin(admin.ModelAdmin):

    ## Define los campos que aparecen al crear o editar un gasto. FECHA no aparece porque se crea automáticamente
    fields = (
        "descripcion",
        "categoria",
        "limite",
    )

    ## Indica las columnas que se mostraran en la tabla de listados del admin
    list_display = (
        "descripcion",
        "categoria",
        "limite",
        "fecha",
    )

    ## Añade una barra lateral para filtrar por categoría
    list_filter = ("categoria", "limite")

    ## Permite buscar por los valores de ese campo
    search_fields = ("categoria",)
    
    ## Para ordenarlos
    ordering = ("limite",)

    ## OJO!! Las opciones que solo afecten a una tupla, DEBEN LLEVAR COMA AL FINAL

## Registramos el modelo
admin.site.register(Expense, ExpenseAdmin)

=======
from django.contrib import admin
from main.models import Expense, ExpenseLin


class ExpenseAdmin(admin.ModelAdmin):
    fields = ("description", "category", "limit", "user")
    list_display = (
        "description",
        "user",
        "category",
        "limit",
        "date",
    )
    list_filter = ("category", "limit")
    search_fields = ("description", "category")
    ordering = ("-date", "description")


class ExpenseLinAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "expense",
        "amount",
        "date",
    )
    list_filter = ("expense",)
    search_fields = ("description",)
    list_editable = ("amount",)


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ExpenseLin, ExpenseLinAdmin)
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25
