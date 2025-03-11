class Wezel:
    def __init__(self, liczba):
        self.liczba = liczba
        self.nastepny = None


class Kolejka:
    def __init__(self):
        self.glowa = None
        self.ogon = None

    def czy_pusta(self):
        if self.glowa is None:
            print('Pusta')
            return True
        return False

    def dodaj(self, liczba):
        print('Dodaję:', liczba)
        nowy = Wezel(liczba)

        if self.czy_pusta():
            self.glowa = self.ogon = nowy
            return

        self.ogon.nastepny = nowy
        self.ogon = nowy

    def usun(self):
        if self.czy_pusta():
            return None

        pomocniczy = self.glowa
        liczba = pomocniczy.liczba
        self.glowa = pomocniczy.nastepny
        print('Usuwam: ', liczba)
        return liczba

    def wypisz(self):
        pomocniczy = self.glowa
        while pomocniczy:
            print(pomocniczy.liczba, '', end='')
            pomocniczy = pomocniczy.nastepny

kolejka = Kolejka()
kolejka.dodaj(5)
kolejka.dodaj(7)
kolejka.dodaj(1)
kolejka.dodaj(9)
kolejka.wypisz()
print(kolejka.usun())
kolejka.wypisz()
print(kolejka.usun())
print(kolejka.usun())
print(kolejka.usun())
print(kolejka.usun())
