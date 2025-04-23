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
            return True
        return False

    def dodaj(self, liczba):
        nowy = Wezel(liczba)
        if self.czy_pusta():
            self.glowa = self.ogon = nowy

        self.ogon.nastepny = nowy
        self.ogon = nowy

    def usun(self):
        if self.czy_pusta():
            return

        pomocniczy = self.glowa
        liczba = pomocniczy.liczba
        self.glowa = self.glowa.nastepny
        return liczba

    def wypisz(self):
        if self.czy_pusta():
            return

        pomocniczy = self.glowa
        while pomocniczy:
            print(pomocniczy.liczba, "", end="")
            pomocniczy = pomocniczy.nastepny
        print()

kolejka = Kolejka()
kolejka.dodaj("abc")
kolejka.dodaj("def")
kolejka.dodaj("ghi")
kolejka.wypisz()

kolejka.usun()
kolejka.usun()
kolejka.wypisz()
