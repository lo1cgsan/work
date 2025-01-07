class Konto:
    def __init__(self, ile=0):
        self.bilans = ile

    def wplata(self, ile):
        self.bilans += ile

    def wyplata(self, ile):
        self.bilans -= ile

    def pobierz_kwote(self, komunikat):
        print(komunikat)
        ile = float(input("Podaj kwotę: "))
        return ile

    def wypisz_bilans(self):
        print(self.bilans)

a = Konto()
a.wypisz_bilans()

b = Konto(100)
b.wypisz_bilans()

