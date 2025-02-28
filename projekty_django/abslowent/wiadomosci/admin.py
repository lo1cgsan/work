from django.contrib import admin
from wiadomosci import models
from django.forms import Textarea
from django.db.models.fields import TextField


@admin.register(models.Wiadomosc)
class WiadomoscAdmin(admin.ModelAdmin):
    exclude = ('autor',)
    formfield_overrides = {
        TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 100})},
    }

    def save_model(self, request, obj, form, change):
        if not change:
            obj.autor = request.user
        obj.save()

