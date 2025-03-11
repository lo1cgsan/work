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
        

def dodaj_ulamki(u1, u2):
    licz = u1.l * u2.m + u2.l * u1.m
    mian = u1.m * u2.m
    return Ulamek(licz, mian)

u1 = Ulamek(7, 8)
u2 = Ulamek(3, 4)
u3 = dodaj_ulamki(u1, u2)
print(f'{u1} + {u2} = {u3}')
