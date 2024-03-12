import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.patches import Circle

fig, ax = plt.subplots()

kolo = Circle((0, 0), 3, fill=False, edgecolor='blue')
ax.add_patch(kolo)

lx = (-3, 3, 3, -3, -3)
ly = (-3, -3, 3, 3, -3)

kwadrat = lines.Line2D(lx, ly, lw=2, color='red')
ax.add_line(kwadrat)

przek1 = lines.Line2D((-3, 3), (-3, 3))
przek2 = lines.Line2D((-3, 3), (3, -3))
ax.add_line(przek1)
ax.add_line(przek2)

ax.scatter(-3, -3, marker='s')
ax.scatter(3, 3, marker='s')
ax.scatter(0, 0, marker='o')

plt.axis('scaled')
plt.show()