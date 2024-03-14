def oblicz_srednia(lista, n):
    suma = 0
    for i in range(n):
        # print(i)
        suma = suma + lista[i]

    srednia = suma / n
    print(srednia)


def oblicz_srednia2(lista, n):
    suma = 0
    for ocena in lista:
        # print(ocena)
        suma = suma + ocena

    srednia = suma / n
    print(srednia)


def oblicz_srednia3(lista):
    suma = sum(lista)
    ile = len(lista)
    print(suma / ile)



def main():
    oceny = [] # utwrzenie pustej listy
    l_ocen = int(input('Podaj liczbę ocen: '))

    for i in range(l_ocen):
        ocena = int(input('Podaj ocenę: '))

        while ocena < 1 or ocena > 6:
            ocena = int(input('Podaj ocenę: '))

        oceny.append(ocena)

    print(oceny)
    oblicz_srednia(oceny, l_ocen)
    oblicz_srednia2(oceny, l_ocen)
    oblicz_srednia3(oceny)



main()
