from django.contrib import admin

# Register your models here.

from .models import Stajaliste, Linija

admin.site.register(Stajaliste)
admin.site.register(Linija)
