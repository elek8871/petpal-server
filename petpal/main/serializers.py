from rest_framework import serializers
from .models import Pet, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name', 'email','password')

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'name', 'breed', 'date of birth', 'nickname', 'catchphrase')