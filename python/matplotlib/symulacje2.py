from math import sqrt
from random import seed, gauss
from time import sleep

start_xy = (0, 0)  # tupla, krotka
n = 100
k = 0.2  # współczynnik długości kroków
dt = 0.05

def ruchy_browna(start_xy, n, k, start_seed):
    seed(start_seed)
    lista_x = [start_xy[0]]
    lista_y = [start_xy[1]]

    for krok in range(1, n):
        dx = lista_x[krok-1] + k * sqrt(dt) * gauss(0, 1)
        dy = lista_y[krok-1] + k * sqrt(dt) * gauss(0, 1)
        lista_x.append(dx)
        lista_y.append(dy)
        sleep(dt)
    
    return (lista_x, lista_y)

punkty = ruchy_browna(start_xy, n, k, 234567)
print(punkty)

def wizualizuj(punkty):
    import matplotlib.pyplot as plt
    
    plt.plot(punkty[0], punkty[1], 'o-')
    plt.show()

wizualizuj(punkty)
