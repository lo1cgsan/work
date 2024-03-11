"""
Napisz program, który pobiera tyle ocen, ile poda użytkownik,
liczy i wypisuje ich średnią.
"""
def oblicz_srednia(oceny, ile_ocen):
    suma = 0

    for i in range(ile_ocen):
        print(i)
        suma += oceny[i]

    srednia = suma / ile_ocen
    print(srednia)


def oblicz_srednia2(lista, n):
    suma = 0

    for element in lista:
        print(element)
        suma += element

    print(suma / n)


def oblicz_srednia3(lista):
    print(sum(lista) / len(lista))


def main():

    ile_ocen = int(input('Ile ocen? '))

    oceny = [] # utworzenie pustej listy

    for i in range(ile_ocen):
        ocena = int(input('Podaj ocenę: '))

        if ocena >= 1 and ocena <=6:
            oceny.append(ocena) # dopisanie elementu do listy
        else:
            ile_ocen = ile_ocen - 1

    print(oceny)

    oblicz_srednia(oceny, ile_ocen)
    print()
    oblicz_srednia2(oceny, ile_ocen)
    print()
    oblicz_srednia3(oceny)


main()
