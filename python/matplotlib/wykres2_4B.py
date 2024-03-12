import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)
    
lista_y = []

lista_x = range(-360, 365, 5)

for x in lista_x:
    y = f(x * np.pi / 180)
    print(y)
    print()
    lista_y.append(y)

plt.plot(lista_x, lista_y)
plt.show()

exit(0)

x = -5
lista_x = [x]
while x < 5.1:
    # print(x)
    x += 0.1
    x = round(x, 1)
    lista_x.append(x)
