import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = 1 / ((x**2) - 1)
    return y
    
lista_y = []

lista_x = np.arange(-5, 5.1, 0.1)
lista_x = [round(x, 1) for x in lista_x]
print(*lista_x)

for x in lista_x:
    y = f(x)
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
