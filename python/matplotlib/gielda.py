from tools import *

import matplotlib.pyplot as plt
import numpy as np

dane = czytaj_csv('dane_gielda.csv', ';')
dane.pop(0)
print(dane)
seria = [float(lista[1].replace(u"\u00a0", '.')) for lista in dane]
print(srednie)