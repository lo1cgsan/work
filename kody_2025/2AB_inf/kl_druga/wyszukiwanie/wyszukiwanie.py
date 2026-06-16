from math import log
import bisect

# algorytm naiwny
def szukaj_naiwnie(dane, szukany):
    for i in range(len(dane)):
        if dane[i] == szukany:
            return i
    return -1

# metoda połowienia, "dziel i zwyciężaj"
def szukaj_binarnie(dane, szukany):
    poczatek = 0
    koniec = len(dane)-1
    licznik = 0

    while poczatek <= koniec:
        licznik = licznik + 1
        print('Licznik:', licznik)
        print(poczatek, koniec)
        srodek = (poczatek + koniec) // 2
        if dane[srodek] == szukany:
            return srodek
        else:
            if szukany < dane[srodek]:
                koniec = srodek - 1
            else:
                poczatek = srodek + 1
    return -1

# wyszukiwanie w zbiorze uporządkowanym
dane = list(range(100))
szukany = 34
print(szukaj_binarnie(dane, szukany))
print(log(len(dane), 2) + 1)
lewy = bisect.bisect_left(dane, szukany)
prawy = bisect.bisect_right(dane, szukany)
print(f'Powtórzeń: {prawy-lewy}')
