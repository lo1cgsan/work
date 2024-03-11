"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik,
liczy i wypisuje ich średnią.
"""
suma = 0
n = int(input('Ile ocen? '))

for i in range(n):
    o1 = int(input('Podaj ocenę: '))

    while o1 < 1 or o1 > 6:
        o1 = int(input('Podaj ocenę: '))

    suma = suma + o1

srednia = suma / n
print(srednia)

