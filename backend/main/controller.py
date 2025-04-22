# Importamos modelo expense creado anteriormente (igual que lo importamos en el Admin)
from main.models import Expense


# Consulta al ORM de Django, devuelve todos los objetos del modelo EXPENSE
# Como hacer un select * from expense
def get_expenses():

    ## Almacenamos el resultado en expenses y lo retornamos
    expenses = Expense.objects.all()
    return expenses

## Esto lo invocamos desde una vista