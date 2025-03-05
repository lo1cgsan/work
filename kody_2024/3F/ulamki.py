class Ulamek:
    def __init__(self, l, m):
    licz: int
    mian: int


def nwd(a, b):
    while a > 0:
        a = a % b
        b = b - a
    return b

def nww(a, b):
    return a * b // nwd(a, b)


def dodaj_ulamki(u1, u2):
    licznik = u1.licz * u2.mian + u2.licz * u1.mian
    mianownik = u1.mian * u2.mian
    return Ulamek(licznik, mianownik)

