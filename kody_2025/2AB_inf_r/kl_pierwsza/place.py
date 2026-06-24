# place.py

# dane wejściowe
lng = int(input('Podaj liczbę nadgodzin: '))
s = float(input('Podaj stawkę za godzinę: '))

# obliczenia
if lng <= 30:
    placa = lng * s
else:
    placa = lng * s + (lng - 30) * s * 0.5

# wyprowadzenie wyniku
print("Płaca:", placa)
