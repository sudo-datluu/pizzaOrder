from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import authenticate

from api.models.users import CustomUser, Staff, Customer, Admin
from api.serializers import CustomUserSerializer, SignUpSerializer, EmployerSerializer

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
        serializer = SignUpSerializer(data=request.data)
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

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def createEmployerAccount(request):
    serializer = EmployerSerializer(data=request.data)
    if serializer.is_valid():
        user_request = request.user
        if isinstance(user_request, CustomUser) and user_request.role != 'A':
            return RESPONSE_FORBIDDEN
        username = request.data.get('username')
        password = request.data.get('password')
        role = request.data.get('role')
        userTbl = {
            'A': Admin(username=username, email=username),
            'S': Staff(username=username, email=username)
        }
        user = userTbl[role]
        user.set_role(role)
        user.set_password(password)
        user.save()
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    else:
        return get_bad_request(msg=serializer.errors)
