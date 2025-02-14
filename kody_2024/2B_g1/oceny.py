# napisz program, który pobierze n ocen
# od użytkownika i wypisze ich średnią
n = int(input('Ile ocen: '))

suma = 0
for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    suma = suma + ocena

print(suma / n)
