# generator liczb pseudolosowych
from random import randint, seed

# seed(12345)
x = randint(1, 10)

for i in range(10):
    y = randint(1, 10)
    if y != x:
        break

for i in range(10):
    z = randint(1, 10)
    if z != x and z != y:
        break

print("Wylosowane:", x, y, z)

n = 5
licznik = 0
for i in range(n):
    a = int(input("Podaj liczbę: "))
    if a == x or a == y or a == z:
        print("Trafiona:", a)
        licznik = licznik + 1


print("Wylosowane:", x, y, z)
print("Liczba trafień:", licznik)
