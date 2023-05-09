from api.models import Order, OrderLine, Product
from .product import ProductSerializer
from .customUser import CustomUserSerializer
from rest_framework import serializers

class OrderLineDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    
    class Meta:
        model = OrderLine
        fields = [
            "product",
            "qty"
        ]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderLineDetailSerializer(many=True)
    customer = CustomUserSerializer()
    class Meta:
        model = Order
        fields = [
            "items",
            "customer",
            "totalPrice"
        ]

class OrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = [
            "product",
            "qty"
        ]

    # def validate(self, data):
    #     product = data["product"]
    #     if product:
    #         raise serializers.ValidationError(
    #             f"Not enough quantity for product {product.name} - max {product.maxQty}"
    #         ) if product.maxQty < data["qty"] else 0
    #     else:
    #         raise serializers.ValidationError("Product do not exist")
        
class CreateOrderSerializer(serializers.ModelSerializer):
    items = OrderLineSerializer(many=True)
    
    class Meta:
        model = Order
        fields = [
            "id",
            "items",
            "totalPrice"
        ]
    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item in items:
            # OrderLineSerializer.validate(item=item)
            OrderLine.objects.create(order=order, **item)
        
        return order