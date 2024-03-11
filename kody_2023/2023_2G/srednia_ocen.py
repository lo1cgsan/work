"""
Napisz program, który pobiera tyle ocen,
ile poda użytkownik oraz
oblicza i wypisuje ich średnią.
"""
ile = int(input("Ile ocen? "))

suma = 0

for i in range(ile):
    ocena = int(input("Podaj ocenę: "))
    suma = suma + ocena

srednia = suma / ile
print(srednia)
