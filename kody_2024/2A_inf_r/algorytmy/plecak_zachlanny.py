from klasa_przedmiot import wczytaj_przedmioty

lista_prz = []  # lista przedmiotów

def pakuj_01(c_max):
    plecak_p = []  # lista zapakowanych przedmiotów

    while  c_max > 0:
        n = 0
        for p in lista_prz:
            if p.w <= c_max:
                n = p
                break
        if n:
            plecak_p.append(n)
            c_max -= n.w
            lista_prz.remove(n)
        else:
            print(f'Brak przedmiotów. Pozostało: {c_max} kg')
            break

    suma_wartosci = 0
    for p in plecak_p:
        print(p)
        suma_wartosci += p.p
    print('Suma wartości:', suma_wartosci)

def main():
    c_max = int(input('Pojemność maks: '))
    wczytaj_przedmioty('dane_plecak.csv', lista_prz, sortuj=True)
    pakuj_01(c_max)

main()
