from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    hobby_1 = models.CharField(blank=True, null=True)
    hobby_2 = models.CharField(blank=True, null=True)
    education = models.CharField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    born_place = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AppUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class schedule(models.Model):
    customer = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
