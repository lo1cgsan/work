"""
Napisz program, który pobiera 3 oceny,
liczy i wypisuje ich średnią.
"""
suma = 0
licznik = 0

o1 = int(input("Podaj ocenę: "))
if o1 > 0 and o1 < 7:
    suma = suma + o1
    licznik = licznik + 1 # inkrementacja

o2 = int(input("Podaj ocenę: "))
if o2 > 0 and o2 < 7:
    suma = suma + o2
    licznik = licznik + 1

o3 = int(input("Podaj ocenę: "))
if o3 > 0 and o3 < 7:
    suma = suma + o3
    licznik = licznik + 1

srednia = suma / licznik
print(srednia)
