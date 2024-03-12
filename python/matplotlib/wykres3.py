import matplotlib.pyplot as plt
import numpy as np

a = float(input("Podaj wsp. a: "))
b = float(input("Podaj wsp. b: "))
c = float(input("Podaj wsp. c: "))

lista_x = range(-10, 11)
lista_y1 = [a * x**2 + b * x + c for x in lista_x]  # ax^2 + bx + c
lista_y2 = [a * x + b for x in lista_x]  # ax + b

plt.axvline()
plt.axhline()
plt.title('Funkcja kwadratowa')
plt.grid()
# plt.plot(lista_x, lista_y1, '.:r', linewidth=4)
# plt.plot(lista_x, lista_y2, '^-b', linewidth=2)
fig, axs = plt.subplots(2)
axs[0].plot(lista_x, lista_y1, '.:r', linewidth=4)
axs[1].plot(lista_x, lista_y2, '^-b', linewidth=2)

plt.show()