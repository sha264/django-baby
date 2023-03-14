from django.contrib import admin

# Register your models here.
from .models import Todo, User
admin.site.register(Todo)
admin.site.register(User)
