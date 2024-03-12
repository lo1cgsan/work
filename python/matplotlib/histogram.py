from tools import *

import matplotlib.pyplot as plt

dane = czytaj_csv('pisemne.csv', ';')
print(dane)
seria = [int(lista[1]) for lista in dane]
print(seria)
n, bins, patches = plt.hist(seria, 15)

plt.xlabel('Wyniki w pkt')
plt.ylabel('Częstość')
plt.show()