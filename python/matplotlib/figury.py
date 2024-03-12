import matplotlib.pyplot as plt
import matplotlib.lines as lines
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

fig, ax = plt.subplots()
lx = (0, 5, 5, 5, 5, 0, 0, 0, 0, 5, 0, 5)
ly = (0, 0, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5)
line = lines.Line2D(lx, ly, lw=2, color="red")
rect = Rectangle((-1, -1), 7, 7, fill=False, edgecolor="green")
circ = Circle((2.5, 2.5), 3.5, fill=False, edgecolor="blue")
ax.add_line(line)
ax.add_patch(rect)
ax.add_patch(circ)
plt.axvline()
plt.axhline()
plt.axis('scaled')
plt.show()