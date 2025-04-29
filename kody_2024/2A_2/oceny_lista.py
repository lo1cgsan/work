# Program pobiera n ocen i wypisuje ich średnią.
n = int(input('Ile ocen: '))

oceny = []  # utworzenie pustej listy

while len(oceny) < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena <= 6 and ocena > 0:
        oceny.append(ocena)
    else:
        print('Błędne dane!')

suma = 0
ocena_min = oceny[0]
ocena_max = oceny[0]
for i in range(n):
    ocena = oceny[i]
    suma += ocena
    if oceny[i] < ocena_min:
        ocena_min = oceny[i]
    if oceny[i] > ocena_max:
        ocena_max = oceny[i]

print('Średnia:', suma / n)
print('Rozpiętość:', ocena_max - ocena_min)
