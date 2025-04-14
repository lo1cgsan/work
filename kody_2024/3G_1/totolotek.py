# totolotek.py
from random import randint

liczby = []  # liczby lodowane
typy = []    # typy użytkownika
n = 6
a = 1
b = 50
trafione = 0

for i in range(n):
    liczba = randint(a, b)
    liczby.append(liczba)

for i in range(n):
    liczba = int(input('Podaj liczbę: '))
    typy.append(liczba)

for i in range(n):
    if typy[i] in liczby:
        trafione += 1

print('Odgadłaś:', trafione)
print(liczby)
