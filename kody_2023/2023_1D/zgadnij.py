from random import randint

licznik = 0
x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)
print(x, y, z)

for i in range(5):
    typ = int(input("Podaj typ: "))
    if typ == x or typ == y or typ == z:
        print("Zgadłeś!")
        licznik = licznik + 1

print("Wylosowano:", x, y, z)
print("Trafionych:", licznik)
