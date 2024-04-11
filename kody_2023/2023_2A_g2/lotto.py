from random import randint

def czy_zapisana(lista, liczba):
    for element in lista:
        if element == liczba:
            return True
    return False


def losuj():
    lista = []
    while len(lista) < 3:
        liczba = randint(1, 10)
        if not czy_zapisana(lista, liczba):
            lista.append(liczba)
    return lista


def pobierz_typy():
    lista = []
    while len(lista) < 5:
        liczba = int(input('Podaj typ: '))
        if not czy_zapisana(lista, liczba):
            lista.append(liczba)
    return lista


def main():
    wylosowane = losuj()
    typy = pobierz_typy()

    licznik = 0
    for typ in typy:
        if czy_zapisana(wylosowane, typ):
            licznik += 1
            print(typ)

    print("Liczba trafionych:", licznik)
    print(wylosowane)


main()
