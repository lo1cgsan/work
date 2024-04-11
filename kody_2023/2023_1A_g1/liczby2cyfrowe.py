"""
Napisz program, który wipisuje i zlicza wszystkie liczby dwucyfrowe
w zakresie <10;100>, w których cyfry nie powtarzają się.
Na końcu wypisz liczbę i sumę takich liczb.

licznik = 0
for i in range(100):
    if i > 9:
        print(i)
        licznik = licznik + 1

licznik = 0
for i in range(10, 100):
    print(i)
    licznik = licznik + 1
"""
licznik = 0
suma = 0
for i in range(1, 10):
    for j in range(10):
        if i != j:
            licznik = licznik + 1
            suma = suma + int(i) * 10 + int(j)
            print(i, j, sep='')
print(licznik, suma)

licznik = 0
suma = 0
for i in range(10,100):
    if i % 11 != 0:
        licznik = licznik + 1
        suma = suma + i
        print(i)
print(licznik, suma)
