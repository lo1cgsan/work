# Model – Widok - Kontroler

# Ustawienia projektu

plik `projekt/settings.py`

# Widoki

`views.py` – widoki

# Adresy URL

`urls.py` – powiązanie adresów url z widokami

https://
www.google.com/
search
?client=firefox-b-lm&q=django

localhost:8000/
localhost:8000/polls/
localhost:8000/polls/5/
localhost:8000/polls/5/results/
localhost:8000/polls/5/vote/

# Modele

`models.py` – modele, tj. klasy definiujące źródła danych

## Migracje

Migracja – zmiana w bazie danych.

- `python3 manage.py makemigrations polls` – przygotowanie migracji aplikacji
- `python3 manage.py sqlmigrate polls 0001` – podgląd migracji
- `python3 manage.py migrate` – zapisanie migracji w bazie



ankiety/urls.py

polls/models.py
polls/urls.py
polls/views.py
polls/admin.py
# Panel administracyjny

`python3 manage.py createsuperuser` – utworzenie konta admina

# Zarządzanie projektem

python3 manage.py runserver
python3 manage.py check

return render(request, "polls/detail.html", {"pytanie": pytanie})

Create
Read
Update
Delete
