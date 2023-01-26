from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'bio',
            'email',
            'first_name',
            'last_name',
            'role'
        )


class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        max_length=150,
        validators=[UnicodeUsernameValidator()]
    )
    email = serializers.EmailField(
        required=True, max_length=254, )

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Использование "me" в имени пользователя запрещено.')
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()
