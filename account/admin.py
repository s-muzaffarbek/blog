from django.contrib import admin
from .models import MyUser

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'birth_day', 'phone']
