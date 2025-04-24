<<<<<<< HEAD
## Funcion de Django que nos permite devolver una plantilla como respuesta
from django.shortcuts import render

#Invocamos la función del archivo controller
from main.controller import get_expenses

## Es una vista basada en función, Django la llama cuando se accede a una URL asociada. REQUEST es el objeto que tiene
## toda la información de la petición HTTP
def index(request):

    ## Llamamos a la función del controller
    expenses = get_expenses()
    ## Recorremos con un bucle for la función y accedemos a los gastos, y los sumamos con sum()
    total = sum(e.limite for e in expenses)

    ## El context es un diccionario que se pasa a la plantilla index.html
    ## expenses contiene todos los gastos
    ## total_expense es una variable para calcular el total gastado
    context = {"expenses": expenses, "total_expense": total}

    ## Devolvemos el HTML de la plantilla index.html con los datos del context
    return render(request, "index.html", context)
=======
from django.shortcuts import render
from main.controllers import get_expenses, get_lines
from django.db.models import Sum


def index(request):
    """
    View function for the index page.
    """

    user = request.user

    expenses = get_expenses(user)

    total_expense = expenses.aggregate(total_expense=Sum("total"))[
        "total_expense"
    ]

    context = {"expenses": expenses, "total_expense": total_expense}

    return render(request, "index.html", context)


def lines(request, expense):
    lines = get_lines(expense_pk=expense)
    context = {"lines": lines}

    return render(request, "lines.html", context)
>>>>>>> bad32a02db6e9749226952f34a9a6794817cfe25
