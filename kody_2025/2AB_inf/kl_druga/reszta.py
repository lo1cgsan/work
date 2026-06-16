# Wydawanie reszty metodą zachłanną

def max_nominal(nominaly, reszta):
    akt_nom = 0
    while akt_nom < len(nominaly) and nominaly[akt_nom] > reszta:
        akt_nom += 1
    return akt_nom


def wydaj_1(nominaly, reszta):
    while reszta > 0:
        # znajdź najw. nominał mniejszy od reszty
        akt_nom = max_nominal(nominaly, reszta)
        if akt_nom >= len(nominaly):
            print('Pozostało:', reszta)
            break
        # oblicz ile razy nominal mieści się w reszcie
        liczba_nom = reszta // nominaly[akt_nom]
        # wypisz liczbę nominalu użytego do wydawania reszty
        print(f'{liczba_nom} * {nominaly[akt_nom]}')
        # pomniejsz resztę
        reszta -= liczba_nom * nominaly[akt_nom]

def wydaj_2(nominaly, reszta):
    ln = []
    for akt_nom in nominaly:
        if akt_nom <= reszta:
            reszta -= akt_nom
            ln.append(akt_nom)
    if reszta > 0:
        return [], reszta
    return ln, 0

def wydaj_3(nominaly, reszta):
    for i in range(len(nominaly)):
        wynik = wydaj_2(nominaly[i:], reszta)
        if wynik[0]:
            print(wynik[0])
            break
    if not wynik[0]:
        print('Pozostało', wynik[1])


# dane wejściowe
nominaly = [5, 2, 2, 2]
reszta = int(input('Podaj resztę: '))

# dane wyjściowe
#wydaj_1(nominaly, reszta)
#wydaj_2(nominaly, reszta)
wydaj_3(nominaly, reszta)
