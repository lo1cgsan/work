from tools import *

import matplotlib.pyplot as plt
import numpy as np

dane = czytaj_csv('dane_klasa1A.csv', ';')
dane.pop(0)
print(dane)
klasy = [lista[0] for lista in dane]
print(klasy)
srednie = [float(lista[1].replace(',', '.')) for lista in dane]
print(srednie)

ile_klas = np.arange(len(klasy))
print(ile_klas)
szerokosc = 0.5
plt.bar(ile_klas, srednie)
plt.ylim([0.1, 6.0])
plt.xticks(ile_klas, klasy)

def p2f(x):
    return float(x.strip('%')) / 100

etykiety = [lista[2] for lista in dane]
frek = [p2f(lista[2]) for lista in dane]
print(frek)
plt.twinx()
plt.plot(frek, color="red")
#wartosci = plt.yticks()
#plt.ylabel(etykiety)
plt.show()