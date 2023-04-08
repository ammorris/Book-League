from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserAdmin

admin.site.register(CustomUser, CustomUserAdmin)
