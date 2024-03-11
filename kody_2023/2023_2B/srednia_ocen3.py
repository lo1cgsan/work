"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik,
liczy i wypisuje ich średnią.
"""
n = int(input('Ile ocen? '))
oceny = [] # utworzenie pustej listy

for i in range(n):
    o1 = int(input('Podaj ocenę: '))

    while o1 < 1 or o1 > 6:
        o1 = int(input('Podaj ocenę: '))

    oceny.append(o1)

print(oceny)
