from rest_framework import serializers
# from django.contrib.auth.models import User  # Не используется
from account.models import CustomUser  # Поменял на вашу CustomUser модель

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        # Создайте пользователя здесь
        return CustomUser.objects.create_user(**validated_data)
