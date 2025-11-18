import matplotlib.pyplot as plt
import numpy as np
from math import sin, pi

def rysuj(x, y, tytul):
    plt.plot(x, y)
    plt.grid()
    plt.axhline()
    plt.axvline()
    plt.title(tytul)
    plt.show()

def fun_liniowa():
    # y = ax + b
    a = int(input('Podaj wsp. a: '))
    b = int(input('Podaj wsp. b: '))
    x = range(-7, 8)
    y = []
    for i in x:
        y.append(a * i + b)
    print(x)
    print(y)
    rysuj(x, y, 'y = ax + b')



def fun_kwadratowa():
    # y = ax^2 + bx + c
    a = int(input('Podaj wsp. a: '))
    b = int(input('Podaj wsp. b: '))
    c = int(input('Podaj wsp. c: '))
    x = range(-7, 8)
    y = []
    for i in x:
        y.append(a * i**2 + b*i + c)
    print(x)
    print(y)
    rysuj(x, y, 'y = ax^2 + bx + c')

def f_tryg():
    x = range(-360, 370, 10)
    print(list(x))
    # y = [sin(st * pi / 180) for st in x]
    y = []
    for st in x:
        y.append(sin(st * pi / 180))
    rysuj(x, y, 'sin(x)')

def f_zlozona():
    """
    Wykonaj wykres funkcji f(x), gdzie x = <-10;10> z krokiem 0.5
    f(x) = x/-3 + a dla x <= 0
    f(x) = x*x/3 dla x > 0
    """
    x = np.arange(-10, 10.5, 0.5)
    a = 2
    print(x)
    y1 = [i / -3 + a for i in x if i <= 0]
    y2 = [i**2 / 3 for i in x if i > 0]
    y = y1 + y2
    print(y)
    rysuj(x, y, 'f(x)')

f_zlozona()
