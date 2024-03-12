import matplotlib.pyplot as plt
import numpy as np

lista_x = range(-360, 370, 10)
#lista_x = [round(x, 1) for x in lista_x]

lista_y1 = []  # np.sin(x * np.pi / 180)
lista_y2 = []  # 3 * sin(x)
lista_y3 = []  # sin(3 * x)
lista_y4 = []  # cos()

for x in lista_x:
    print(x)
    lista_y1.append(np.sin(x * np.pi / 180))
    lista_y2.append(3 * np.sin(x * np.pi / 180))
    lista_y3.append(np.sin(3 * x * np.pi / 180))
    lista_y4.append(np.cos(x * np.pi / 180))

plt.axvline()
plt.axhline()
plt.title('Funkcje trygonometryczne')
plt.xlabel('Stopnie')
plt.grid()
plt.xticks(range(-360, 370, 90))
plt.plot(lista_x, lista_y1, 'o:c')
#plt.plot(lista_x, lista_y2)
#plt.plot(lista_x, lista_y3)
plt.plot(lista_x, lista_y4, color='g', linewidth=5)
plt.show()