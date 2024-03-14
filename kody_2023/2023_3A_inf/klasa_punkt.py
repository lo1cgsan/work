class Punkt:
    def __init__(self, n, x=0, y=0):
        self.nazwa = n
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.nazwa}({self.x},{self.y})'


def pobierz_punkty(punkty, nazwy):
    for n in nazwy:
        p = Punkt(n)
        p.x = float(input(f'{n}: podaj x: '))
        p.y = float(input(f'{n}: podaj y: '))
        punkty.append(p)
