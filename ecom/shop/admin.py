from django.contrib import admin
from .models import Products,Order

# Register your models here.
admin.site.register(Order)
admin.site.register(Products)