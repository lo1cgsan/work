from django.contrib.messages import success
from django.urls import path
from . import views  # import widoków aplikacji
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name="index"),
    path('rejestruj/', CreateView.as_view(
        template_name='czat/rejestruj.html',
        form_class=UserCreationForm,
        success_url='/'),
        name="rejestruj"),
    path("loguj/", auth_views.LoginView.as_view(template_name="czat/loguj.html"), name='loguj'),
    path('wyloguj/', auth_views.LogoutView.as_view(), name='wyloguj'),
]
