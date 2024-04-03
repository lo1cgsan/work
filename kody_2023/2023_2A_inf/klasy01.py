from osoba_klasa import Osoba


class Konto(Osoba):
    liczba_kont = 0

    def __init__(self, imie='', ile=0):
        super().__init__(imie)
        self.bilans = ile
        Konto.liczba_kont += 1

    def wplata(self, ile):
        self.bilans += ile
        return self.bilans

    def wyplata(self, ile):
        if self.bilans - ile >= 0:
            self.bilans -= ile
        else:
            print('Brak środków')
        return self.bilans

    def __str__(self):
        return self.imie + ': ' + str(self.bilans)


osoba1 = Konto('Ewa', 100)
osoba2 = Konto('Adam', 50)
print(Konto.liczba_kont)
osoba1.wplata(50)
osoba2.wplata(50)
osoba1.set_pesel('123456789')
osoba1.wyplata(300)
osoba2.wyplata(20)
print('Konto:', osoba1)
print('Konto:', osoba2)

