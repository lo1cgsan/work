from django.contrib import admin

from .models import Pytanie, Choice
# Register your models here.

admin.site.register(Pytanie)
admin.site.register(Choice)
