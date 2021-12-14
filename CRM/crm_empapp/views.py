from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework import permissions


class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    lookup_field = "id"
    queryset = Users.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_field = "id"
    queryset = Users.objects.all()


class EmployeeAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "id"
    queryset = Employee.objects.all()


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "id"
    queryset = Employee.objects.all()
