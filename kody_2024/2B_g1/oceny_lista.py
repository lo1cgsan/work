# Program pobiera n ocen i zapisuje w liście.
# Program powinien sprawdzać poprawność danych.

n = int(input('Ile ocen: '))
oceny = []

for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    if ocena >= 1 and ocena <= 6:
        oceny.append(ocena)
    else:
        print('Błędna ocena!')

suma = 0
for ocena in oceny:
    suma += ocena

print('Średnia:', suma/len(lista))
