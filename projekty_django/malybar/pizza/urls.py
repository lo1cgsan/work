from django.urls import path
from . import views  # import widoków aplikacji

app_name = 'pizza'  # przestrzeń nazw aplikacji
urlpatterns = [
    path('', views.index, name='pizza_index'),
]
