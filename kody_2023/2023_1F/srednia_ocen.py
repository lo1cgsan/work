"""
Napisz program, który pobiera 10 ocen,
liczby i wypisuje ich średnią.
"""
suma = 0
licznik = 0
ile_ocen = int(input("Ile ocen? "))

for i in range(ile_ocen):
    o1 = int(input("Podaj ocenę: "))
    if o1 > 0 and o1 <= 6:
        suma = suma + o1
        licznik = licznik + 1

srednia = suma / licznik

print(srednia)
