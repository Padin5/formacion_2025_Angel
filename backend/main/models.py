## Importamos el módulo para poder trabajar con modelos
from django.db import models

## Importamos una funcion de traduccion, para traducir etiquetas o campos usando _("Texto a traducir")
from django.utils.translation import gettext_lazy as _

## Los modelos son básicamente Clases, dentro de la programación orientada a objetos, que representan un modelo de BBDD
## Importamos la superclase 'models' de Django
class Expense(models.Model):

## Definimos los atributos de clase
    ## Charfield por ejemplo sería el tipo cadena de texto y tenemos que definir su longitud, hay muchos más parámetros a definir
    descripcion = models.CharField(max_length=255, verbose_name=_("Description"))
    limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Limit"))
    fecha = models.DateTimeField(auto_created=True, verbose_name=_("Date"))

    ## Los choices son Arrays y funcionan como tuplas, valor guardado -> texto mostrado.
    ## Funciona como un formulario, solo se guardará un valor seleccionado
    categoria = models.CharField(max_length=100, choices=[
        ('FOOD', 'Food'),
        ('TRAN', 'Transport'),
        ('ENTR', 'Entertainment'),
        ('UTIL', 'Utilities'),
        ('OTHR', 'Other')
    ], 
    verbose_name=_("Category"))

    ## La clase Meta representa los metadatos del modelo, cómo se llama el modelo en el Admin
    ## Con ordering definimos el orden en que se mostraran los objetos de la BBDD
    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")
        ordering = ["-fecha"]
        

    ## Esta funcion nos retorna los objetos que se mostraran en el admin de django, tomando los datos de la BBDD
    def __str__(self):
        return f"{self.descripcion} - {self.limite} - {self.fecha} - {self.categoria}"


class ExpenseLines(models.Model) :
    
    ## Related_name para acceder a las cabeceras desde las líneas de gasto
    gasto = models.ForeignKey(Expense, on_delete=models.CASCADE, related_name="linea", verbose_name=_("line"))
    concepto = models.CharField(max_length=255, verbose_name=_("concept"))
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("cuantity"))
    fecha = models.DateTimeField(auto_created=True, verbose_name=_("date"), null=True)

    class Meta:
        verbose_name = _("ExpenseLine")
        verbose_name_plural = _("ExpenseLines")
    
    def __str__(self):
        return f"{self.concepto} - {self.cantidad}"