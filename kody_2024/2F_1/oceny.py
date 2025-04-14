# Program pobiera n ocen i wypisuje ich średnią.

n = int(input('Ile ocen: '))

suma = 0
licznik = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    if ocena <= 6 and ocena >= 1:
        suma += ocena
        licznik += 1

srednia = suma / licznik

print(srednia)
