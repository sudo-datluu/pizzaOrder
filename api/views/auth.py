from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from api.models.users import CustomUser, Staff, Customer
from api.serializers import CustomUserSerializer, CustomerSignUpSerializer

from .const import RESPONSE_FORBIDDEN, RESPONSE_NOT_FOUND, get_bad_request

'''
Login for customer, admin and staff only
'''
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(username=username)
            if authenticate(
                request=request,
                username=username,
                password=password
            ) and user:
                refreshToken = RefreshToken.for_user(user)
                accessToken = refreshToken.access_token
                tokenData = {
                    'refresh': str(refreshToken),
                    'access': str(accessToken)
                }
                serializer = CustomUserSerializer(user)
                return Response(
                    serializer.data | tokenData
                )
            else:
                return RESPONSE_FORBIDDEN
        except CustomUser.DoesNotExist:
            return RESPONSE_NOT_FOUND

'''
Sign up for customer
'''
class CustomerSignUp(APIView):
    def post(self, request):
        serializer = CustomerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')
            customer = Customer(username=username, email=username)
            customer.set_role('C')
            customer.set_password(password)
            customer.save()

            serializer = CustomUserSerializer(customer)
            return Response(serializer.data)
        else:
            return get_bad_request(msg=serializer.errors)