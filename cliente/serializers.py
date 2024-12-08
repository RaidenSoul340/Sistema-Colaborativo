from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("nome", "senha", "email")
        extra_kwargs = {"senha": {"write_only": True}}
        
    def create(self, validated_data):
        validated_data["senha"] = make_password(validated_data("senha"))
        return User.objects.create(**validated_data)