import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Ellipse
from matplotlib.patches import Shadow

fig, ax = plt.subplots()

elip = Ellipse((7, 2.5), 4, 2, color="orange")
ax.add_patch(elip)

kolo = Circle((2, 2.5), 1.5, fill=False, edgecolor='orange', lw=2)
ax.add_patch(kolo)
kolo_cien = Shadow(kolo, -0.03, -0.04)
ax.add_patch(kolo_cien)

dane = np.array([[0, 5], [5, 9], [10, 5]])
poly = Polygon(dane, closed=True, fill=False, edgecolor="red", lw=3)
ax.add_patch(poly)

rect = Rectangle((0, 0), 10, 5, fill=False, edgecolor="green", lw=3)
ax.add_patch(rect)

plt.axis('scaled')
plt.show()