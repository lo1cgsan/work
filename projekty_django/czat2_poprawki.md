## Poprawki w czat2/settings.py:

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

## Poprawki w pliku czat/urls.py:
from django.urls import reverse_lazy

    path('rejestruj/', CreateView.as_view(
        template_name='czat/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/czat/'),
        name="rejestruj"),
    path("loguj/", auth_views.LoginView.as_view(template_name="czat/loguj.html"), name='loguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),

## Poprawka w pliku (czat/index.html):

    {% if user.is_authenticated %}
      <p>Jesteś zalogowany jako {{ user.username }}.</p>
      <p><a href="{% url 'czat:wyloguj' %}">Wyloguj się</a></p>
    {% else %}
      <p><a href="{% url 'czat:loguj' %}">Zaloguj się</a></p>
      <p><a href="{% url 'czat:rejestruj' %}">Zarejestruj się</a></p>
    {% endif %}

## Poprawka w pliku czat/admin.py:

from . import models
