from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .utils import get_and_authenticate_user
from .models import BlogCustomUser
from .serializers import (
    BlogCustomUserSerializer,
    LoginSerializer,
    AuthSerializer,
    ResetPasswordSerializer,
    UpdateProfileSerializer
)


class BlogCustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BlogCustomUserSerializer
    queryset = BlogCustomUser.objects.all()


class UserCreate(APIView):
    serializer_class = BlogCustomUserSerializer

    def post(self, request, format='json'):
        serializer = BlogCustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            json = {}
            json['username'] = serializer.data['username']
            json['email'] = serializer.data['email']
            json['token'] = token.key
            return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format='json'):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = get_and_authenticate_user(**serializer.validated_data)
            data = AuthSerializer(user).data
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(generics.UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    model = BlogCustomUser
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():

            if not self.object.check_password(serializer.validated_data.get("old_password")):
                return Response({"old_password": ["incorrect password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(
                serializer.validated_data.get("password1"))
            self.object.save()

            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfie(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    model = BlogCustomUser
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()

        serializer = UpdateProfileSerializer(data=request.data)
        if serializer.is_valid():

            response = {
                'message': 'No Changes were made.',
                'data': []
            }

            if serializer.validated_data.get("email"):
                self.object.updateEmail(serializer.validated_data.get("email"))
                self.object.save()

                response['message'] = 'Profile updated successfully'
                response['data'].append("email:"+self.object.email)

            if serializer.validated_data.get("bio"):
                self.object.updateBio(serializer.validated_data.get("bio"))
                self.object.save()

                response['message'] = 'Profile updated successfully'
                response['data'].append("bio:"+self.object.bio)

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
