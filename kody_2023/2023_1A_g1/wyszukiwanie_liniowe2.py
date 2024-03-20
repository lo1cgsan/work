# generator liczb pseudolosowych
from random import randint, seed

# seed(12345)
x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

"""
Napisz program, który pobiera z klawiatury 5 liczb,
sprawdza czy podana liczba równa jest którejś z wylosowanych
i jeżeli zlicz trafienia i wypisuje odgadnięte liczby.
"""
n = 5
licznik = 0
for i in range(n):
    a = int(input("Podaj liczbę: "))
    if a == x:
        print("Trafiona:", a)
        licznik = licznik + 1
    if a == y:
        print("Trafiona:", a)
        licznik = licznik + 1
    if a == z:
        print("Trafiona:", a)
        licznik = licznik + 1

print("Wylosowane:", x, y, z)
print("Liczba trafień:", ...)
