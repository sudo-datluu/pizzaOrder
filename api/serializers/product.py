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