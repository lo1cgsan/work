# Program pobiera n ocen i wypisuje ich średnią.

n = int(input('Ile ocen: '))

suma = 0
licznik = 0

for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    if ocena <= 6 and ocena > 0:
        suma += ocena
        licznik += 1

if licznik != 0:
    srednia = suma / licznik
    print(srednia)
else:
    print('Poprawne oceny głąbie są w zakresie 1-6!')
