# Importamos el serializador del REST de Django
from rest_framework import serializers
# Importamos los modelos a serializar
from main.models import Expense, ExpenseLines

# Con este serializer transformamos CADA LINEA DE GASTO a JSON
class ExpenseLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseLines
        fields = (
            "gasto",
            "concepto",
            "cantidad",
            "fecha",
        )


class ExpenseSerializer(serializers.ModelSerializer):

    # Aqui es donde entra en juego el related_name de la foreign key!!
    lines = ExpenseLinesSerializer(many=True, required=False)
    
    # Campos de solo lectura, definidos en el modelo Expanse
    total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )
    total_pedidos = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Expense
        fields = (
            "id",
            "description",
            "category",
            "limit",
            "date",
            "total",
            "lines",
        )