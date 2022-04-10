from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(jugadores)
admin.site.register(entrenadores)
admin.site.register(sponsors)