class Ulamek:
    def __init__(self, l, m):
        self.l = l
        self.m = m
        self.nwd = self.nwd()

    def __str__(self):
        return f'{self.l}/{self.m}'

    def nwd(self):
        a = self.l
        b = self.m
        while a > 0:
            a = a % b
            b = b - a
        return b

    def __add__(self, u):
        licz = self.l * u.m + u.l * self.m
        mian = self.m * u.m
        return Ulamek(licz, mian)

    def __sub__(self, u):
        licz = self.l * u.m - u.l * self.m
        mian = self.m * u.m
        return Ulamek(licz, mian)

    def __mul__(self, u):
        return Ulamek(self.l * u.l, self.m * u.m)

    def __floordiv__(self, u):
        return Ulamek(self.l * u.m, self.m * u.l)

    def skroc(self):
        self.l = self.l // self.nwd
        self.m = self.m // self.nwd

u1 = Ulamek(4, 8)
u2 = Ulamek(3, 4)
u3 = u1 // u2
u3.skroc()
print(f'{u1} // {u2} = {u3}')
