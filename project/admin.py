from django.contrib import admin

# Register your models here.
from .models import Event, Blog

admin.site.register(Event)
admin.site.register(Blog)