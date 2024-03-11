"""
Napisz program, który pobiera 3 oceny,
liczy i wypisuje ich średnią.
"""
suma = 0
licznik = 0


for i in 'abc':
    o1 = int(input("Podaj ocenę: "))
    if o1 > 0 and o1 < 7:
        suma = suma + o1
        licznik = licznik + 1 # inkrementacja


srednia = suma / licznik
print(srednia)
