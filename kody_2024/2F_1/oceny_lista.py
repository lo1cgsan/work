# Program pobiera n ocen i wypisuje ich średnią.

n = int(input('Ile ocen: '))

oceny = []  # utworzenie pustej listy

while len(oceny) < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena <= 6 and ocena >= 1:
        oceny.append(ocena)
    else:
        print('Błędne dane!')

suma = 0
for i in range(len(oceny)):
    ocena = oceny[i]
    suma += ocena

print('Średnia:', suma / n)
