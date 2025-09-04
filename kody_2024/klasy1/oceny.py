# Program oblicza średnią 10 podanych ocen.

n = int(input('Ile ocen? '))

suma = 0
for i in range(n):
    ocena = int(input(f'Podaj ocenę {i+1}: '))
    suma = suma + ocena

srednia = suma / n

print('Średnia:', srednia)
