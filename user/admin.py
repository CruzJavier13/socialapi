from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserAuth, User

# Register your models here.
admin.site.register(CustomUserAuth, UserAdmin)
admin.site.register(User)
