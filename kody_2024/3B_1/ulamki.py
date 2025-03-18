# ulamki.py
class Ulamek:
    def __init__(self, licznik, mianownik):
        self.l = licznik
        self.m = mianownik
        self.nwd = Ulamek.nwd(self.l, self.m)

    @staticmethod
    def nwd(a, b):
        while a > 0:
            a = a % b
            b = b - a
        return b

    @staticmethod
    def nww(a, b):
        return (a * b) // Ulamek.nwd(a, b)

    def __add__(self, u):
        licznik = self.l * u.m + u.l * self.m
        mianownik = self.m * u.m
        return Ulamek(licznik, mianownik)

    def __sub__(self, u):
        licznik = self.l * u.m - u.l * self.m
        mianownik = self.m * u.m
        return Ulamek(licznik, mianownik)

    def __mul__(self, u):
        return Ulamek(self.l * u.l, self.m * u.m)

    def __floordiv__(self, u):
        return Ulamek(self.l * u.m, self.m * u.l)

    def __str__(self):
        return f'{self.l}/{self.m}'

    def skroc(self):
        self.l = self.l // self.nwd
        self.m = self.m // self.nwd

u1 = Ulamek(1, 2)
u2 = Ulamek(3, 4)
u3 = u1 + u2
print(u3, u3.nwd)
u3.skroc()
print(u3)
print(u2 - u1)
print(u1 * u2)
print(u1 // u2)
