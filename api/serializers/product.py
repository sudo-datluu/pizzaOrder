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
            "caloriesPerUnit",
            "img_url"
        ]

    def getSerialFromID(self, productID):
        product = Product.objects.get(id=productID)
        return ProductSerializer(product)
    
class PizzaSerializer(serializers.ModelSerializer):
    pizzaBase = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()
    topping = serializers.SerializerMethodField()
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
            "topping",
            "img_url"
        ]
    
    def get_pizzaBase(self, obj):
        return obj.get_pizzaBase_display()

    def get_size(self, obj):
        return obj.get_size_display()

    def get_topping(self, obj):
        return obj.get_topping_display()