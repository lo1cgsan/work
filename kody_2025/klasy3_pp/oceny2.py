# Program pobiera n ocen i wypisuje ich średnią.
n = int(input('Ile ocen: '))

suma = 0
licznik = 0

while licznik < n:
    ocena = int(input('Podaj ocenę: '))
    if ocena <= 6 and ocena > 0:
        suma += ocena
        licznik += 1
    else:
        print('Błędne dane!')

if licznik != 0:
    srednia = suma / licznik
    print(srednia)
else:
    print('Poprawne oceny są w zakresie 1-6!')
