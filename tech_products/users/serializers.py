from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        username = f"{validated_data['first_name'].lower()}.{validated_data['last_name'].lower()}"
        password = validated_data.pop('password')
        email = validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email address must be unique.")

        user = User(username=username, **validated_data)
        user.set_password(password)
        user.save()
        return user
