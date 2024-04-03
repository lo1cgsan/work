class Osoba:

    def __init__(self, imie, nazwisko='', wiek=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.ustaw_plec(imie)

    def ustaw_plec(self, imie):
        if self.imie[-1] == 'a':
            self.plec = 'k'
        else:
            self.plec = 'm'

    def set_pesel(self, pesel):
        self.pesel = pesel

o1 = Osoba('Jan', 'Kowalski')
