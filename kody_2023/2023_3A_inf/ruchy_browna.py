from random import randint
from math import pi, cos, sin, sqrt


def losuj_punkty(n, r, lx, ly):
    x, y = 0, 0
    for i in range(n):
        k = randint(0, 360) * pi / 180
        x = x + cos(k) * r
        y = y + sin(k) * r
        lx.append(x)
        ly.append(y)
    s = sqrt(x**2 + y**2)
    return s


def pokaz_wykres(lx, ly, s):
    pass


def main():
    n = int(input('Ile ruchów? '))
    r = 1
    lx, ly = [0], [0]
    s = losuj_punkty(n, r, lx, ly)
    pokaz_wykres(lx, ly, s)
    print(*zip(lx, ly))
    print('Przesunięcie:', s)


main()
