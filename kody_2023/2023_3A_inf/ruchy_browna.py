from random import randint
from math import pi, cos, sin, sqrt
import matplotlib.pyplot as plt

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
    plt.plot(lx, ly, 'go:')
    plt.plot((0, lx[-1]), (0, ly[-1]), 'rs-', lw=2)
    plt.axvline()
    plt.axhline()
    plt.show()


def main():
    n = int(input('Ile ruchów? '))
    r = 1
    lx, ly = [0], [0]
    s = losuj_punkty(n, r, lx, ly)
    print(*zip(lx, ly))
    print('Przesunięcie:', s)
    pokaz_wykres(lx, ly, s)


main()
