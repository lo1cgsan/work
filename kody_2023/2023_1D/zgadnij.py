from random import randint

"""
1) Napisz program, który losuje 3 liczby z zakresu <1;10>,
2) pobiera 5 typów użytkownika,
3) jeżeli użytkownik odgadł którąś liczbę, wypisuje "Zgadłeś",
4) a na końcu wypisuje wylosowane liczby oraz liczbę trafień.
"""
licznik = 0
x = randint(1, 10)
y = randint(1, 10)
z = randint(1, 10)
print(x, y, z)

for i in range(5):
    typ = int(input("Podaj typ: "))
    if typ == x:
        print("Zgadłeś!")
        licznik = licznik + 1
    if typ == y:
        print("Zgadłeś!")
        licznik = licznik + 1
    if typ == z:
        print("Zgadłeś!")
        licznik = licznik + 1

print("Wylosowano:", x, y, z)
print("Trafionych:", licznik)
