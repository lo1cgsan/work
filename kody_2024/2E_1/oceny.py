# Napisz progam, który pobiera 3 oceny i wypisuje ich  średnią.

n = int(input('Ile ocen: '))

suma = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    suma = suma + ocena

srednia = suma / n

print('Średnia:', srednia)
