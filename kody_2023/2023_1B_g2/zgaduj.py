from random import randint

x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)

licznik = 0
for i in range(3):
    typ = int(input("Podaj typ: "))
    if typ == x or typ == y or typ == z:
        print('zgadłeś')
        licznik = licznik + 1

print(x, y, z)
print("Liczba trafionych:", licznik)
