from django.forms import ModelForm
from .models import Pytanie

class OdpowiedzForm(ModelForm):
    class Meta:
        model = Pytanie
        exclude = ('glosy',)
