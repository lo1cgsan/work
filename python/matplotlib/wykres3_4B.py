import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.sin(x)

def f2(x):
    return 3 * np.sin(x)

lista_y1 = []
lista_y2 = []
lista_y3 = []
lista_y4 = []

lista_x = range(-360, 365, 5)  # generowanie wartości x
# lista_x = [x * np.pi / 180 for x in lista_x]  # zamiana stopni na radiany

# wyliczanie wartości y
for x in lista_x:
    lista_y1.append(f(np.radians(x)))
#    lista_y2.append(f(3 * x))
#    lista_y3.append(f2(x))
    lista_y4.append(np.cos(np.radians(x)))

plt.axhline()  # oś x
plt.axvline()  # oś y
plt.xticks(range(-360, 365, 60))
plt.plot(lista_x, lista_y1)
plt.plot(lista_x, lista_y4)

#plt.plot(lista_x, lista_y2)
#plt.plot(lista_x, lista_y3)

#fig, axs = plt.subplots(3)
#axs[0].plot(lista_x, lista_y1)
#axs[1].plot(lista_x, lista_y2)
#axs[2].plot(lista_x, lista_y3)

plt.show()
