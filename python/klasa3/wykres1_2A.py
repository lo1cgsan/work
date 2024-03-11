import matplotlib.pyplot as plt
import numpy as np

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))

lista_x = range(-10, 11)
lista_y = []

for x in lista_x:
    lista_y.append(a * x**2 + b * x + c)

print(*lista_x)
print(*lista_y)

plt.axhline()
plt.axvline()
plt.grid()
plt.plot(lista_x, lista_y)
plt.show()

