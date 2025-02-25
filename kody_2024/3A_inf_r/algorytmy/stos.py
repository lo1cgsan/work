class Wezel:
    def __init__(self, liczba):
        self.liczba = liczba
        self.nastepny = None


class Stos:
    def __init__(self):
        self.wierzcholek = None

    def czy_pusty(self):
        if self.wierzcholek is None:
            print('Pusty')
            return True
        return False

    def odloz(self, liczba):
        print('Odkładam:', liczba)
        nowy = Wezel(liczba)
        toDO: nowy.nastepny = self.wierzcholek
        self.wierzcholek = nowy

    def zdejmij(self):
        if self.czy_pusty():
            return None
        pomocniczy = self.wierzcholek
        liczba = pomocniczy.liczba
        self.wierzcholek = pomocniczy.nastepny
        print('Zdejmuję:', liczba)
        return liczba

    def wypisz(self):
        pomocniczy = self.wierzcholek
        while pomocniczy:
            print(pomocniczy.liczba, '', end='')
            pomocniczy = pomocniczy.nastepny

stos = Stos()
stos.odloz(5)
stos.odloz(7)
stos.odloz(1)
stos.odloz(9)
stos.wypisz()

