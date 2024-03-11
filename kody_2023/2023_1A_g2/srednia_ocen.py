"""
Napisz program, który pobiera 10 ocen,
liczy i wypisuje ich średnią.
"""
suma = 0
licznik = 0

n = int(input("Ile ocen? "))

for i in range(n):
    print(i)
    o1 = int(input("Podaj ocenę: "))
    if o1 > 0 and o1 < 7:
        suma = suma + o1
        licznik = licznik + 1

srednia = suma / licznik

print(srednia)
