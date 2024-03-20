class Konto:
    def __init__(self, imie='', ile=0):
        self.imie = imie
        self.bilans = ile

    def wplata(self, ile):
        self.bilans += ile
        return self.bilans

    def wyplata(self, ile):
        if self.bilans - ile >= 0:
            self.bilans -= ile
        else:
            print('Brak środków')
        return self.bilans

    def set_pesel(self, pesel):
        self.pesel = pesel

    def __str__(self):
        return self.imie + ': ' + str(self.bilans)


osoba1 = Konto('Ewa', 100)
osoba2 = Konto('Adam', 50)
osoba1.wplata(50)
osoba2.wplata(50)
osoba1.wyplata(300)
osoba2.wyplata(20)
print('Konto:', osoba1)
print('Konto:', osoba2)

