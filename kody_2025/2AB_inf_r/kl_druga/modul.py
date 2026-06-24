import random

def pobierz_liczbe(kom):
    znaki = input(kom).strip()
    if znaki.isnumeric():
        liczba = int(znaki)
        return liczba
    else:
        print('Błędne dane!')
        return False

def pobierz_znaki(kom, dozwolone):
    znaki = input(kom).strip()
    for z in znaki:
        if z not in dozwolone:
            print('Błędne dane!')
            return False
    return znaki

def pobierz_dane(kom):
    znaki = input(kom).strip()
    try:
        liczba = int(znaki)
        return liczba
    except ValueError:
        print('Błędne dane!')
        return False

def czy_w_liscie(lista, wartosc):
    for elem in lista:
        if elem == wartosc:
            return True
    return False


def czy_w_liscie2(lista, wartosc):
    for i in range(len(lista)):
        if lista[i] == wartosc:
            return True
    return False


def losuj_liczby(n, maks):
    liczby = []
    # losowanie liczb
    while len(liczby) < n:
        liczba = random.randint(0, maks)
        # if czy_w_liscie(liczby, liczba):
        if liczba in liczby:
            print('Powtórzona liczba!')
        else:
            liczby.append(liczba)
    return liczby


def pobierz_typy(n, maks):
    """
    """
    typy = []
    # for i in range(n):
    while len(typy) < n:
        typ = pobierz_liczbe('Podaj typ: ')
        if typ == False:
            continue
        if 0 <= typ <= maks:
            typy.append(typ)
        else:
            print('Błędny zakres!')
    return typy


def sprawdz_trafione(typy, liczby):
    # sprawdzanie liczby trafień
    trafione = []
    for typ in typy:
        if czy_w_liscie2(liczby, typ):
        # if typ in liczby:
            trafione.append(typ)
    return trafione
