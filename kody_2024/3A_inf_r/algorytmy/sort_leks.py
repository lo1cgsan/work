class Wezel:
    def __init__(self, wyraz):
        self.wyraz = wyraz
        self.nastepny = None
        self.poprzedni = None

class Lista:
    def __init__(self):
        self.glowa = None
        self.ogon = None

    def czy_pusta(self):
        return not self.glowa

    def dodaj(self, wyraz):
        print('Dodaję:', wyraz)
        nowy = Wezel(wyraz)

        if self.czy_pusta():
            self.glowa = self.ogon = nowy
            self.glowa.nastepny = self.ogon.nastepny = nowy
            return

        self.ogon.nastepny = nowy
        nowy.poprzedni = self.ogon
        self.ogon = nowy

    def usun(self, wezel):
        if wezel == self.glowa and self.glowa.nastepny != None:
            self.glowa = self.glowa.nastepny
            self.glowa.poprzedni = None
            return

        if wezel == self.ogon:
            wezel.poprzedni.nastepny = None
            self.ogon = wezel.poprzedni
        else:
            wezel.poprzedni.nastepny = wezel.nastepny
            wezel.nastepny.poprzedni = wezel.poprzedni

    def wypisz(self):
        pomocniczy = self.glowa
        while pomocniczy.nastepny != None:
            print(pomocniczy.wyraz, '', end='')
            pomocniczy = pomocniczy.nastepny
        print(pomocniczy.wyraz)

    def porownaj(self, w1, w2):
        wyraz_1 = w1.wyraz.lower()
        wyraz_2 = w2.wyraz.lower()

        if wyraz_1 > wyraz_2:
            return 1
        elif wyraz_1 < wyraz_2:
            return -1
        else:
            return 0

    def sortuj(self):
        pomocniczy = self.glowa
        while True:
            if pomocniczy.nastepny == None:
                break
            if self.porownaj(pomocniczy, pomocniczy.nastepny) > 0:
                self.usun(pomocniczy)
                self.wstaw(pomocniczy)
                pomocniczy = self.glowa
            else:
                pomocniczy = pomocniczy.nastepny

    def wstaw(self, wezel):
        pomocniczy = wezel.nastepny
        while pomocniczy != self.ogon and self.porownaj(wezel, pomocniczy.nastepny) >= 0:
            pomocniczy = pomocniczy.nastepny

        if pomocniczy == self.ogon:
            wezel.nastepny = None
            wezel.poprzedni = self.ogon
            self.ogon.nastepny = wezel
            self.ogon = wezel
        else:
            wezel.poprzedni = pomocniczy
            wezel.nastepny = pomocniczy.nastepny
            pomocniczy.nastepny.poprzedni = wezel
            pomocniczy.nastepny = wezel

dane = ['sql', 'cpp', 'Python', 'zzz', 'Java']

lista = Lista()
for wyraz in dane:
    lista.dodaj(wyraz)

lista.wypisz()
lista.sortuj()
lista.wypisz()
