from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import login
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from knox.views import LoginView as KnoxLoginView


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = "id"
    queryset = User.objects.all()


class EmployeeAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "id"
    queryset = Employee.objects.all()
