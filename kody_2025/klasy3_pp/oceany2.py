# Program pobiera n ocen i wypisuje ich średnią.

n = int(input('Ile ocen: '))

suma = 0
licznik = 0
while licznik < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena >= 1 and ocena <= 6:
        suma += ocena
        licznik += 1
    else:
        print('Błędne dane!')

srednia = suma / licznik

print(srednia)
