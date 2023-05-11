from api.models.users.customUser import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    def get_role(self, obj):
        return obj.get_role_display()
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "role"
        ]
    
    