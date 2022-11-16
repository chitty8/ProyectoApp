from django.contrib import admin

from .models import Equipo, Jugadores, Avatar

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Jugadores)
admin.site.register(Avatar)
