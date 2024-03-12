from tools import *
import matplotlib.pyplot as plt
import numpy as np

dane = czytaj_csv('dane_klasa1A.csv')
dane.pop(0)
print(dane)

seria = [float(rekord[1].replace(',', '.')) for rekord in dane]
print(seria)

klasy = [rekord[0] for rekord in dane]

ile_kolumn = np.arange(len(seria))
plt.bar(ile_kolumn, seria, 0.9)
plt.xticks(ile_kolumn, klasy)

frekwencje = [float(rekord[2].replace('%', '')) / 100 for rekord in dane]
print(frekwencje)

plt.twinx()
plt.plot(frekwencje, color="red")

frek_etykiety = [str(i) + '%' for i in range(0, 101, 10)]
locs = np.arange(0, 1.1, 0.1)  #[0, 0.1, 0.2, ..., 1]
plt.yticks(locs, frek_etykiety)

plt.ylabel("Wartości procentowe frekwencji")
plt.show()