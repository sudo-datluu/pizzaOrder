from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Product, Pizza
from api.serializers import ProductSerializer, PizzaSerializer

from .const import RESPONSE_NOT_FOUND

class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:100]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class PizzaList(APIView):
    def get(self, request, format=None):
        products = Pizza.objects.all()[:100]
        serializer = PizzaSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
            return product if product.category != 'PZ' else Pizza.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, product_id, format=None):
        try:
            product = self.get_object(product_id=product_id)
            serializer = ProductSerializer(product) if product.category != 'PZ' else PizzaSerializer(product)
            return Response(serializer.data)
        except Http404:
            return RESPONSE_NOT_FOUND

@api_view(['POST'])
def search_product(request):
    keyword = request.data.get('keyword', '')
    if keyword:
        products = Product.objects.filter(Q(name__icontains=keyword))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return ProductList.get()

@api_view(['GET'])
def get_top_products(request):
    products = [Product.objects.filter(category=cat).first() for cat in Product.Category]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)