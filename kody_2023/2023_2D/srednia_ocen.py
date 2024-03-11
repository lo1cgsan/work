"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik,
liczy i wypisuje ich średnią.
"""
def oblicz_srednia(lista, n):
    suma = 0
    for i in range(n):
        print(i)
        suma = suma + lista[i]

    print(suma / n)


def oblicz_srednia2(lista):
    print(sum(lista) / len(lista))


ile_ocen = int(input('Ile ocen? '))
oceny = [] # utworzenie pustej listy

for i in range(ile_ocen):
    ocena = int(input('Podaj ocenę: '))
    if ocena > 0 and ocena < 7:
        oceny.append(ocena) # dopisz element do listy
    else:
        ile_ocen = ile_ocen - 1

print(oceny)
oblicz_srednia(oceny, ile_ocen)
print()
oblicz_srednia2(oceny)
