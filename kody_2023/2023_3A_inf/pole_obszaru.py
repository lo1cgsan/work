from math import fabs
import matplotlib.pylab as plt

def fun(x):
    return x * x


def fun2(x):
    return x * x - 10


def oblicz_pole(a, b, d, f):
    w = (b - a) / d
    p = 0
    for i in range(1, d+1):
        x = a + w * i - w / 2
        p += w * fabs(f(x))

    return p


def wykres(a, b, f):
    lx = range(int(a), int(b)+1)
    ly = [f(x) for x in lx]

    plt.plot(lx, ly, '.-b')
    plt.grid() # siatka wykresu
    plt.axhline()
    plt.axvline()
    plt.xlabel('Oś x')
    plt.ylabel('x^2')
    plt.axvline(x=a, linewidth=2, color='g')
    plt.axvline(x=b, linewidth=2, color='g')
    plt.show()


def main():
    f = fun2
    a, b = 0, 0
    while b <= a:
        a = float(input('Podaj lewy: '))
        b = float(input('Podaj prawy: '))
    d = int(input('Podaj liczbę przedziałów: '))
    print(oblicz_pole(a, b, d, f))
    wykres(a, b, f)

main()