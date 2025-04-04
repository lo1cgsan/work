# Napisz progam, który pobiera 3 oceny i wypisuje ich  średnią.

def srednia(oceny, n):
    for i in range(n):
        print(oceny[i])
    toDo:

n = int(input('Ile ocen: '))
oceny = []  # utworzenie pustej listy

for i in range(n):
    ocena = int(input('Podaj ocenę: '))
    oceny.append(ocena)

print(oceny)
