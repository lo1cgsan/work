# zapis_odczyt.py

def zapisz_dane(nazwa_pliku, dane, tryb):
    with open(nazwa_pliku, tryb) as plik:
        for el in dane:
            plik.write(el+'\n')
    # plik.close()


def odczytaj_dane(nazwa_pliku):
    dane = []
    with open(nazwa_pliku, 'r') as plik:
        for linia in plik:
            print(linia.strip())
            dane.append(linia.strip())
    return dane


dane = 'ala ma kota'
zapisz_dane('litery.txt', dane, 'a')
odczytaj_dane('litery.txt')
