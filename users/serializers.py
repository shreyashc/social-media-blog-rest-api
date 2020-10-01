from rest_framework import serializers
from .models import BlogCustomUser
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token


class BlogCustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(
            queryset=BlogCustomUser.objects.all(), message="email is already registred")]
    )

    username = serializers.CharField(
        validators=[UniqueValidator(
            queryset=BlogCustomUser.objects.all(), message="username is already taken")]
    )

    bio = serializers.CharField(max_length=255, required=False)

    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = BlogCustomUser.objects.create_user(
            validated_data['email'], validated_data['username'], validated_data['password'])
        return user

    class Meta:
        model = BlogCustomUser
        fields = ('id', 'username', 'email', 'password', 'bio')
        read_only_fields = ['id']


class AuthSerializer(serializers.ModelSerializer):

    auth_token = serializers.SerializerMethodField()

    class Meta:
        model = BlogCustomUser
        fields = ('id', 'username', 'email', 'auth_token')

    def get_auth_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        print(token)
        return token.key


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class ResetPasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True, write_only=True)
    password1 = serializers.CharField(
        required=True, min_length=8, write_only=True)
    password2 = serializers.CharField(
        required=True, min_length=8, write_only=True)

    def validate(self, attrs):
        print(attrs)
        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError("passwords don't match.")
        return attrs


class UpdateProfileSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=False,
        validators=[UniqueValidator(
            queryset=BlogCustomUser.objects.all(), message="email is already registred")]
    )

    bio = serializers.CharField(
        required=False
    )
