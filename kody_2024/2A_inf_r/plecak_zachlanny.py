from klasa_przedmiot import wczytaj_przedmioty

lista_prz = []  # lista przedmiotów

def pakuj_01(c_max):
    plecak_p = []  # lista zapakowanych przedmiotów

    while  c_max > 0:
        pass

def main():
    c_max = int(input('Pojemność maks: '))
    wczytaj_przedmioty('dane_plecak.csv', lista_prz, sortuj=True)
    pakuj_01(c_max)

main()
