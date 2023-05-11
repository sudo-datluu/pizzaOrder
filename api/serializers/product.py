from api.models import Product, Pizza
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "get_absolute_url",
            "description",
            "maxQty",
            "pricePerUnit",
            "caloriesPerUnit"
        ]

    def getSerialFromID(self, productID):
        product = Product.objects.get(id=productID)
        return ProductSerializer(product)
    
class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = [
            "id",
            "category",
            "name",
            "get_absolute_url",
            "description",
            "maxQty",
            "pricePerUnit",
            "caloriesPerUnit",
            "pizzaBase",
            "size",
            "topping"
        ]