class Ulamek:
    def __init__(self, l=1, m=1):
        self.licznik = l
        self.mianownik = m

    def nwd(self):
        a = self.licznik
        b = self.mianownik
        while a > 0:
            a = a % b
            b = b - a
        return b

    def skroc(self):
        nwd = self.nwd()
        if nwd > 1:
            self.licznik = self.licznik // nwd
            self.mianownik = self.mianownik // nwd

    def __str__(self):
        return f'{self.licznik} / {self.mianownik}'


def mnoz_ulamki(u1, u2):
    pass


def dodaj_ulamki(u1, u2):
    pass


def odejmij_ulamki(u1, u2):
    pass


u1 = Ulamek(3, 9)
u2 = Ulamek(5, 7)
print(u1, u2)

u1.skroc()
u2.skroc()
print(u1, u2)

print(mnoz_ulamki(u1, u2))




