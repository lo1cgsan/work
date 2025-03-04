class Wezel:
    def __init__(self, pozycja):
        self.pozycja = pozycja
        self.nastepny = None

class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None

    def czy_pusta(self):
        return not self.glowa

    def dodaj(self, pozycja):
        print('Dodaję:', pozycja)
        nowy = Wezel(pozycja)

        if self.czy_pusta():
            self.glowa = self.ogon = nowy
            self.glowa.nastepny = self.ogon.nastepny = nowy
            return

        self.ogon.nastepny = nowy
        self.ogon = nowy
        self.ogon.nastepny = self.glowa

    def usun(self, pozycja):
        if self.glowa.pozycja == pozycja:
            self.ogon.nastepny = self.glowa.nastepy
            self.glowa = self.glowa.nastepny
            return

        pomocniczy1 = self.glowa
        while pomocniczy1 != self.ogon and pomocniczy1.nastepny.pozycja != pozycja:
            pomocniczy1 = pomocniczy1.nastepny

        if pomocniczy1.nastepny.pozycja == pozycja:
            pomocniczy2 = pomocniczy1.nastepny
            pomocniczy1.nastepny = pomocniczy2.nastepny  # eliminacja węzła pomocniczy2
            if pomocniczy2 == self.ogon:
                self.ogon = pomocniczy1
        else:
            print('Brak węzła!')

    def wypisz(self):
        pomocniczy = self.glowa
        while pomocniczy.nastepny != self.glowa:
            print(pomocniczy.pozycja, '', end='')
            pomocniczy = pomocniczy.nastepny
        print(pomocniczy.pozycja)

    def przejdz(self, krok, wezel=None):
        pass
