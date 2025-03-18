class Ulamek:
    def __init__(self, l, m):
        self.l = l
        self.m = m
        self.nwd = Ulamek.nwd(l, m)

    def __str__(self):
        return f'{self.l}/{self.m}'

    def skroc(self):
        self.l = self.l // self.nwd
        self.m = self.m // self.nwd

    @staticmethod
    def nwd(a, b):
        while a > 0:
            a = a % b
            b = b - a
        return b

    @staticmethod
    def nww(a, b):
        return a * b // Ulamek.nwd(a, b)

    def __add__(self, u2):
        licznik = self.l * u2.m + u2.l * self.m
        mianownik = self.m * u2.m
        return Ulamek(licznik, mianownik)

    def __sub__(self, u2):
        licznik = self.l * u2.m - u2.l * self.m
        mianownik = self.m * u2.m
        return Ulamek(licznik, mianownik)

    def __mul__(self, u2):
        return Ulamek(self.l * u2.l, self.m * u2.m)

    def __floordiv__(self, u2):
        return Ulamek(self.l * u2.m, self.m * u2.l)

u1 = Ulamek(1, 2)
u2 = Ulamek(3, 4)
u3 = u1 + u2
u3.skroc()
print(u3)
print(u1 + u2)
print(u1 - u2)
print(u1 * u2)
print(u1 // u2)
