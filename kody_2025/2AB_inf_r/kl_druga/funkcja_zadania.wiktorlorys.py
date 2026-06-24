import numpy as np
import matplotlib.pyplot as plt
from math import pi
from math import tan
from math import cos
from math import sqrt

def rysuj(x, y, tytul):
    plt.figure()         
    plt.plot(x, y)
    plt.title(tytul)
    plt.xlabel('x')
    plt.ylabel('wartość funkcji')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.show()
    

def fun_zadanie5():
    tytul = "2*cos(x)"
    x = range(0, 370, 10)
    x = list(x)
    y = []
    for i in x:
        y.append(2 * cos(i * pi / 180))
    rysuj(x, y, tytul)

def fun_zadanie6():
    tytul = "cot(x)"
    x = range(0, 370, 10)
    x = list(x)
    x.remove(0)
    x.remove(180)
    x.remove(360)
    y = []
    for i in x:
        y.append(1 / tan(i * pi /180))
    rysuj(x, y, tytul)

def fun_zadanie7():
    tytul = "3 * peirwiastek(x)"
    x = range(0, 370, 10)
    x = list(x)
    y = []
    for i in x:
        y.append(3 * sqrt(i))
    rysuj(x, y, tytul)

fun_zadanie5()
fun_zadanie6()
fun_zadanie7()