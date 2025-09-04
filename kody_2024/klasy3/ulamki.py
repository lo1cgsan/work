# ulamki.py
class Ulamek:
    def __init__(self, l, m):
        self.l = l
        self.m = m
        self.nwd = self.nwd()
        self.l = self.l // self.nwd
        self.m = self.m // self.nwd

    def nwd(self):
        a = self.l
        b = self.m
        while a > 0:
            a = a % b
            b = b - a
        return b

    def __add__(self, u2):
        licz = self.l * u2.m + u2.l * self.m
        mian = self.m * u2.m
        return Ulamek(licz, mian)

    def __sub__(self, u2):
        licz = self.l * u2.m - u2.l * self.m
        mian = self.m * u2.m
        return Ulamek(licz, mian)

    def __mul__(self, u2):
        return Ulamek(self.l * u2.l, self.m * u2.m)

    def __floordiv__(self, u2):
        return Ulamek(self.l * u2.m, self.m * u2.l)

    def __str__(self):
        return f'{self.l}/{self.m}'


u1 = Ulamek(2, 8)
u2 = Ulamek(2, 4)
u3 = u1 + u2
print(u3)
u4 = u1 - u2
print(u4)
print(u3 * u4)
