# srednie.py
# Napisz program, który oblicza średnią
# n ocen podanych przez użytkownika.
n = int(input('Ile ocen: '))
suma = 0

for i in range(n):
    print('Powtórzenie:', i)
    ocena = int(input('Podaj ocenę: '))
    suma = suma + ocena

print(suma/n)
