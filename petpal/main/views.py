from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, PetSerializer
from .models import User
from .models import Pet

# Create your views here.

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class PetView(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()