
n = int(input('Ile ocen: '))

oceny = []  # utworzenie pustej listy

while len(oceny) < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena >= 1 and ocena <= 6:
        oceny.append(ocena)
    else:
        print('Błędne dane!')

print(oceny)
# odczytywanie elementów listy
suma = 0
for i in range(n):
    ocena = oceny[i]
    suma += ocena

print('Średnia:', suma / n)
