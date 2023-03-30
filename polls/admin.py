from django.contrib import admin
from .models import Poll, Choice, Pokemon, trainer, CampoDeBatalha

admin.site.register(Poll)
admin.site.register(Pokemon)
admin.site.register(trainer)
admin.site.register(CampoDeBatalha)

