class Ulamek:
    def __init__(self, l, m):
        self.l = l
        self.m = m
        self.nwd = nwd(l, m)

    def __str__(self):
        return f'{self.l}/{self.m}'

    def skroc(self):
        self.l = self.l // self.nwd
        self.m = self.m // self.nwd

def nwd(a, b):
    while a > 0:
        a = a % b
        b = b - a
    return b

def nww(a, b):
    return a * b // nwd(a, b)

def dodaj_ulamki(u1, u2):
    licznik = u1.l * u2.m + u2.l * u1.m
    mianownik = u1.m * u2.m
    return Ulamek(licznik, mianownik)

def mnoz_ulamki(u1, u2):
    licznik = u1.l * u2.l
    mianownik = u1.m * u2.m
    return Ulamek(licznik, mianownik)

u1 = Ulamek(7, 8)
u2 = Ulamek(3, 5)
u3 = dodaj_ulamki(u1, u2)
u3.skroc()
print(f'{u1} + {u2} = {u3}')
u4 = mnoz_ulamki(u1, u2)
u4.skroc()
print(f'{u1} * {u2} = {u4}')

