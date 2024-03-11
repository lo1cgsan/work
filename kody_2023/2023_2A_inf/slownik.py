import csv
import json
import os


def zapisz_slownik(n_pliku, slownik):
    # plik = open(n_pliku, 'w')
    with open(n_pliku, 'w') as plik:
        for w in slownik:
            znaczenia = ' '.join(slownik[w])
            wiersz = w + ':' + znaczenia
            print(wiersz, file=plik)
    # wyraz:znaczenia1,znaczenie2
    # plik.close()


def zapisz_csv(n_pliku, slownik, d=','):
    with open(n_pliku, 'w', encoding='utf-8') as plik:
        plik_csv = csv.writer(plik, delimiter=d)
        for w_obcy in slownik:
            znaczenia = ' '.join(slownik[w_obcy])
            plik_csv.writerow((w_obcy, znaczenia))


def odczytaj_csv(n_pliku, slownik, d=','):
    if not czy_jest(n_pliku):
        return

    with open(n_pliku, 'r', encoding='utf-8') as plik:
        plik_csv = csv.reader(plik, delimiter=d)
        for rekord in plik_csv:
            znaczenia = rekord[1].split(' ')
            slownik[rekord[0]] = znaczenia


def czy_jest(n_pliku):
    if not os.path.isfile(n_pliku):
        print(f'Plik {n_pliku} nie istnieje!')
        return False
    return True

def pobierz_znaczenia():
    znaczenia = input('Podaj znaczenia oddzielone spacjami:\n')
    znaczenia = znaczenia.split(' ')
    znaczenia = [w.strip() for w in znaczenia]
    return znaczenia



def main():
    n_pliku = 'slownik.csv'
    slownik = {}  # pusty słownik
    odczytaj_csv(n_pliku, slownik)
    print(slownik)

    slowo = input('Podaj słowo: ').strip()

    while slowo:
        slownik[slowo] = pobierz_znaczenia()
        slowo = input('Podaj słowo: ').strip()

    print(slownik)
    zapisz_slownik(n_pliku, slownik)
    zapisz_csv(n_pliku, slownik)


main()
