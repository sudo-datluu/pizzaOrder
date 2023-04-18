from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Product
from api.serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetail(APIView):
    def get_object(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, product_id, format=None):
        product = self.get_object(product_id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['POST'])
def search_product(request):
    keyword = request.data.get('keyword', '')
    if keyword:
        products = Product.objects.filter(Q(name__icontains=keyword))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return ProductList.get()