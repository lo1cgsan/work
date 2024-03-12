import numpy as np

lista_x = np.arange(-5, 5.1, 0.1)
lista_y = []
for x in lista_x:
    lista_y.append(1 / (x**2 - 1))

print(lista_x, lista_y)


