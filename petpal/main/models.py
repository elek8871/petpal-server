from django.db import models

# User Model
class User(models.Model):
    name = models.CharField(max_length=50) 
    email = models.EmailField(max_length=200) 
    password = models.CharField(max_length=50) 

def __str__(self):
    return self.name

class Pet(models.Model):
    name = models.CharField(max_length=100) 
    breed = models.CharField(max_length=100) 
    date_of_birth = models.DateField()
    nickname = models.CharField(max_length=100) 
    catchphrase = models.CharField(max_length=250) 

def __str__(self):
    return self.name
