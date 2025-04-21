from django.db import models

## Importamos una funcion de traduccion
from django.utils.translation import gettext_lazy as _

## Los modelos son básicamente Clases, dentro de la programación orientada a objetos
## Importamos la superclase 'models' de Django
class Expense(models.Model):

## Definimos los atributos de clase
    ## Charfield por ejemplo sería el tipo char (String) y tenemos que definir su longitud, hay muchos más parámetros a definir
    descripcion = models.CharField(max_length=255, verbose_name=_("Description"))
    limite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Limit"))
    fecha = models.DateTimeField(auto_created=True)

    ## Los choices son Arrays y funcionan como tuplas, solo nos dejará introducir los caracteres definidos
    categoria = models.CharField(max_length=100, choices=[
        ('FOOD', 'Food'),
        ('TRAN', 'Transport'),
        ('ENTR', 'Entertainment'),
        ('UTIL', 'Utilities'),
        ('OTHR', 'Other')
    ], verbose_name=_("Category"))

    def __str__(self):
        return f"{self.descripcion} - {self.limite} - {self.fecha} - {self.categoria}"


