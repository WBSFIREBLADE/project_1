from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'Mobile_No']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value
    
    def validate_Mobile_No(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError   (
            "Mobile number must be exactly 10 digits."
            )
        return value    

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            Mobile_No=validated_data.get("Mobile_No")
        )
    

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            token = RefreshToken(self.token)
            token.blacklist()
        except Exception:
            raise serializers.ValidationError("Invalid or expired refresh token.")
    

