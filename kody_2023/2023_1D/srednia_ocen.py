"""
srednia_ocen.py
Napisz program, który pobiera 10 ocen,
liczy i wypisuje ich średnią.
"""
suma = 0
licznik = 0

for i in range(10):
    o1 = int(input("Podaj ocenę: "))
    if o1 >= 1 and o1 <= 6:
        suma = suma + o1
        licznik = licznik + 1

srednia = suma / licznik
print(srednia)
