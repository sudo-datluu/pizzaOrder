from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions, status
from rest_framework.views import APIView

from django.http import Http404
from api.models import Customer, Order, CustomUser
from api.serializers import CreateOrderSerializer, OrderSerializer

from .const import RESPONSE_NOT_FOUND, RESPONSE_FORBIDDEN, get_bad_request
'''
Create new order
'''
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_order(request):
    serializer = CreateOrderSerializer(data=request.data)
    if serializer.is_valid():
        customer = Customer.objects.get(username=request.user.username)
        if not customer:
            return RESPONSE_FORBIDDEN
        try:
            serializer.save(customer=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return get_bad_request(serializer.errors)
    
    return get_bad_request(serializer.errors) 

'''
Get order
'''
class OrderDetail(APIView):
    def get_object(self, order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise Http404
        
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, order_id, format=None):
        try:
            user = Customer.objects.filter(username=request.user.username).first() or CustomUser.objects.filter(username=request.user.username).first()
            order = self.get_object(order_id=order_id)
            if not user and ( (not user.is_employer()) or (order.customer != user)):
                return RESPONSE_FORBIDDEN
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Http404:
            return RESPONSE_NOT_FOUND

'''
Get order
'''
class FullfillOrder(APIView):
    def get_object(self, order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            raise Http404
        
    @permission_classes([permissions.IsAuthenticated])
    def post(self, request, order_id, format=None):
        try:
            user = Customer.objects.filter(username=request.user.username).first() or CustomUser.objects.filter(username=request.user.username).first()
            order = self.get_object(order_id=order_id)
            if not user and ( (not user.is_employer()) or (order.customer != user)):
                return RESPONSE_FORBIDDEN
            order.status = 'FF'
            order.save()
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        except Http404:
            return RESPONSE_NOT_FOUND

'''
Get order of a customer
'''
class CustomerOrderList(APIView):
    @permission_classes([permissions.IsAuthenticated])
    def get(self, request, customer_id, format=None):
        user = CustomUser.objects.filter(username=request.user.username).first()
        
        if not user and (
            (not user.is_employer()) or
            (user.id != customer_id)
        ): 
            return RESPONSE_FORBIDDEN
        customer = Customer.objects.filter(id=customer_id).first()
        orders = Order.objects.filter(customer=customer)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
