from ssl import DefaultVerifyPaths
from django.contrib import admin

from .models import Appointments, Daily, Pet_Diary, User, Health
from .models import Pet

# Register your models here.
admin.site.register(User)
admin.site.register(Pet)
admin.site.register(Pet_Diary)
admin.site.register(Health)
admin.site.register(Daily)
admin.site.register(Appointments)

class User(admin.ModelAdmin):
    list_display = ('id','username', 'email','password')

class Pet (admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'date_of_birth', 'nickname', 'catchphrase','user')

class Health(admin.ModelAdmin):
    list_display = ("id","visit_date", "visit_type", "pet_weight","shots", "medicine", "other","tx_plan","pet")

class Daily(admin.ModelAdmin):
    list_display = ("id","food_schedule", "walk_schedule", "potty_trips", "medicine_schedule", "pet")

class Appointments(admin.ModelAdmin):
    list_display = ("id", "grooming", "play_date", "cuddles", "pet")
