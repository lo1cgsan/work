from math import pi, cos, sin
from random import seed, randint

start_xy = (0, 0)  # tupla, krotka
n = 150
k = 360  # wielokrotność kąta 360/k
wektor = 1.0

def ruchy_browna(start_xy, n, wektor, start_seed):
    seed(start_seed)
    lista_x = [start_xy[0]]
    lista_y = [start_xy[1]]

    for krok in range(1, n):
        fi = randint(0, k-1) * 2 * pi / k
        
        dx = lista_x[krok-1] + wektor * cos(fi)
        dy = lista_y[krok-1] + wektor * sin(fi)

        lista_x.append(dx)
        lista_y.append(dy)
    
    return (lista_x, lista_y)

punkty = ruchy_browna(start_xy, n, wektor, 234567)
print(punkty)

def wizualizuj(punkty):
    import matplotlib.pyplot as plt
    
    plt.plot(punkty[0], punkty[1], 'o-')
    plt.show()

wizualizuj(punkty)
