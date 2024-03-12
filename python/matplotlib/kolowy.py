from tools import *
import matplotlib.pyplot as plt

dane = czytaj_csv('dane_wybory.csv', ';')
print(dane)

# etykiety = []
# for rekord in dane:
#     etykiety.append(rekord[0])

etykiety = [rekord[0] for rekord in dane]
frakcje = [rekord[1] for rekord in dane]
kolory = ['grey', 'green', 'blue', 'red']
explode = [0, 0, 0, 0.05]

fig, ax = plt.subplots()
fig.set_size_inches(9, 7)
fig.canvas.manager.set_window_title("Wykres kołowy")

patches, t1 = ax.pie(frakcje, explode=explode, labels=etykiety, colors=kolory)

plt.legend(patches, etykiety, loc="upper right")
plt.show()