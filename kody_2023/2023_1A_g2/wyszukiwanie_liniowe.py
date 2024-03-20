# generator liczb pseudolosowych
from random import randint, seed

# seed(12345)
x = randint(0, 10)
y = randint(0, 10)
z = randint(0, 10)

"""
Napisz pętlę, która pobierze 5 liczb z klawiatury
i policzy, ile liczb odgadł użytkownik. Wypisz odgadnięte liczby,
a po pętli wylosowane liczby oraz liczbę odgadniętych.
"""
n = 5
licznik = 0
for i in range(n):
    a = int(input("Podaj liczbę: "))
    if a == x:
        print("Trafiłem:", a)
        licznik = licznik + 1
    elif a == y:
        print("Trafiłem:", a)
        licznik = licznik + 1
    elif a == z:
        print("Trafiłem:", a)
        licznik = licznik + 1

print("Wylosowane:", x, y, z)
print("Odgadniętych:", licznik)
