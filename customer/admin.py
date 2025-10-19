from django.contrib import admin

# Register your models here.

from .models import Customer, AppUser

admin.site.register(Customer)
admin.site.register(AppUser)