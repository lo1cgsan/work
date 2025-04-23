class Przedmiot:
    """
    w - waga w kg
    p - wartość przedmiotu
    v - opłacalność
    """

    licz_prz = 1  # licznik przedmiotów

    def __init__(self, w, p):
        self.w = w
        self.p = p
        self.v = p / w
        self.id = Przedmiot.licz_prz
        Przedmiot.licz_prz += 1

    def __str__(self):
        return f'P{self.id}: w/p/v: {self.w}/{self.p}/{self.v}'

def zwroc_wartosc(przedmiot):
    return przedmiot.p

def wczytaj_przedmioty(n_pliku, lista_prz, sortuj=[False]):
    import csv
    with open(n_pliku, newline='') as plik:
        for r in csv.reader(plik, delimiter=';'):
            r = list(map(float, r))
            lista_prz.append(Przedmiot(r[0], r[1]))

    if sortuj:
        lista_prz.sort(key=lambda przedmiot: przedmiot.v, reverse=True)
