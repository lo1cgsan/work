# suma_liczb.py
# Pobieraj liczby, aż do momentu kiedy podasz 5 liczb parzystych.
# wypisz ich sumę.

suma = 0
licznik = 0

while licznik < 5:
    liczba = int(input('Podaj liczbę: '))
    if liczba % 2 == 0:
        licznik += 1  # inkrementacja
        suma += liczba

print(f'Suma: {suma}. Licznik: {licznik}.')
