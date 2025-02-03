from rest_framework import serializers
from .models import RegisterUser

class RegisterSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    city = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return RegisterUser.objects.create(**validated_data)