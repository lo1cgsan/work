from random import randint
from math import pi, cos, sin, sqrt

import matplotlib.pyplot as plt

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

def wykres(l_p, s):
    lx = [0]
    ly = [0]
    for p in l_p:
        lx.append(p.x)
        ly.append(p.y)

    plt.plot(lx, ly, "o:g")
    plt.grid()
    plt.axvline()
    plt.axhline()
    plt.xlabel("Oś x")
    plt.ylabel("Oś y")
    plt.title("Ruchy Browna")

    plt.show()

def losuj_punkty(n, r, l_p):
    x, y = 0, 0
    # l_p.append(Punkt(0, 0))
    for i in range(n):
        k = randint(0, 360) * pi / 180
        x = x + cos(k) * r
        y = y + sin(k) * r
        l_p.append(Punkt(x, y))
    s = sqrt(x**2 + y**2)
    return s

def main():
    n = int(input('Ile ruchów? '))
    r = 1
    l_p = []  # lista punktów
    s = losuj_punkty(n, r, l_p)
    print(*l_p)
    wykres(l_p, s)

main()