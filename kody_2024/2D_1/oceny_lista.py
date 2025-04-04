# oceny_lista.py

def srednia(oceny, n):
    suma = 0
    for i in range(n):
        suma += oceny[i]
    print('Średnia:', suma / n)

oceny = []  # utworzenie pustej listy

n = int(input('Ile ocen? '))

for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    oceny.append(ocena)

print(oceny)
