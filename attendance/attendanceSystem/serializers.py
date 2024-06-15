# serializers.py
from rest_framework import serializers
from .models import User, Roster, Attendance
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "is_staff", "is_manager")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            is_staff=validated_data["is_staff"],
            is_manager=validated_data["is_manager"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            refresh = RefreshToken.for_user(user)
            return {
                "username": user.username,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        raise serializers.ValidationError("Invalid credentials")


class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roster
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ["user", "timestamp", "image"]
        read_only_fields = ["timestamp"]
