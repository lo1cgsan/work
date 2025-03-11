# ulamki.py
class Ulamek:
    def __init__(self, licznik, mianownik):
        self.l = licznik
        self.m = mianownik

def nwd(a, b):
    while a > 0:
        a = a % b
        b = b - a
    return b

def nww(a, b):
    return (a * b) / nwd(a, b)

def dodaj(u1, u2):
    licznik = u1.l * u2.m + u2.l * u1.m
    mianownik = u1.m * u2.m
    return Ulamek(licznik, mianownik)

u1 = Ulamek(1, 2)
u2 = Ulamek(3, 4)
