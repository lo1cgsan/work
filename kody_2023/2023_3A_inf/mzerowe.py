import numpy as np
import matplotlib.pyplot as plt

def fun1(x):
    # return 2 * x - 4
    return 2 * x - 4


def fun2(x):
    return 2 * x ** 2 - 4 * x


def wykres(a, b, f):
    lx = np.linspace(a, b, 30)
    ly = [f(x) for x in lx]
    plt.plot(lx, ly, ".-b")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


def mzerowe(a, b, d, f):
    # f(c) > d
    while b - a > d and f(a) != 0 and f(b) != 0:
        c = (a + b) / 2
        print(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b

    return c

# dane wejściowe
f = fun1

lewy = prawy = 0
while f(lewy) * f(prawy) > 0:
    lewy = float(input("Podaj lewy: "))
    prawy = float(input("Podaj prawy: "))

d = float(input("Podaj dokładność: "))

wykres(lewy, prawy, f)

wynik = mzerowe(lewy, prawy, d, f)
print("Wynik:", wynik, "f(wynik) =", f(wynik))

