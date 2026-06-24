def ile_liczb(lista_znakow):
    licznik = 0
    for el in lista_znakow:
        el = el.replace(',', '.')
        try:
            liczba = float(el)
            licznik += 1
        except:
            pass
    return licznik


def ile_liczb_2(lista_znakow):
    licznik = 0
    for el in lista_znakow:
        if el[0].isdigit():
            licznik += 1
    return licznik


plik_danych = 'dane1.txt'

with open(plik_danych) as plik:
    for wiersz in plik:
        dane = wiersz.strip().split('\t')
        print(dane)
        print(ile_liczb(dane))
        print(ile_liczb_2(dane))
