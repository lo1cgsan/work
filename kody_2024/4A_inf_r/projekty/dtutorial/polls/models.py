import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Pytanie(models.Model):
    tekst_pytania = models.CharField(max_length=200)
    pub_date = models.DateTimeField("data publikacji")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.tekst_pytania


class Choice(models.Model):
    question = models.ForeignKey(Pytanie, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
