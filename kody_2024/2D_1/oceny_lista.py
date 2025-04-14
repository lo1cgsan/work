# oceny_lista.py
# Program pobiera n ocen i wypisuje średnią.
# Program powinien sprawdzać poprawność danych.

def srednia(oceny, n):
    suma = 0
    for i in range(n):
        print('Pozycja:', i)
        suma += oceny[i]
    print('Średnia:', suma / n)

oceny = []  # utworzenie pustej listy

n = int(input('Ile ocen? '))

licznik = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    if ocena > 0 and ocena <=6:
        oceny.append(ocena)
        licznik += 1
    else:
        print('Błędna ocena!')

print(oceny)
# wywołanie funkcji
srednia(oceny, licznik)
