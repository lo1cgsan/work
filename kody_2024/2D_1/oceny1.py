# oceny1.py
# Napisz program, który pobiera 20 ocen i wypisuje ich średnią.

n = int(input('Ile ocen? '))

suma = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    suma += ocena

srednia = suma / n
print(srednia)
