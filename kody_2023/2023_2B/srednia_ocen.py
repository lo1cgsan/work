"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik,
liczy i wypisuje ich średnią.
"""

suma = 0
n = int(input('Ile ocen? '))
n = 3

for i in range(n):
    o1 = int(input('Pobierz ocenę: '))

    if o1 > 0 and o1 < 7:
        suma = suma + o1
    else:
        n = n - 1

if n > 0:
    srednia = suma / n
    print(srednia)
else:
    print("Brak ocen!")

