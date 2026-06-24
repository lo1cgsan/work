# Napisz funkcję min_max(), która wyszukuje i zwraca
# najmniejszy lub największy element w zbiorze.
import random

def min_max(dane, tryb=True):
    """
    Przeszukiwanie liniowe
    @param tryb – jeżeli True zwraca wartość najmniejszą
    w przeciwnm razie największą
    """
    wynik = dane[0]

    for el in dane:
        if tryb:
            if el < wynik:
                wynik = el
        elif el > wynik:
            wynik = el

    return wynik

# napisz funkcje wyszukaj_min_max(), która za pomocą metody połowienia
# wyszukuje element min i maks jednocześnie

dane = random.sample(range(0, 101), 10)
print(dane)
print(min_max(dane))
print(min_max(dane, False))
