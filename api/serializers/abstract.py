from rest_framework import serializers
from django.contrib.auth.models import User
import django.contrib.auth.password_validation as validators
from django.core import exceptions
import re
# from validate_email import validate_email

class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(max_length=255, required=True, write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already existed")
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(regex, value):
            raise serializers.ValidationError("Invalid email format")
    
    def validate_password(self, value):
        try:
             # validate the password and catch the exception
            validators.validate_password(password=value)

         # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(list(e))

class EmployerSerializer(SignUpSerializer):
    role = serializers.ChoiceField(choices=['S', 'A'], required=True) 