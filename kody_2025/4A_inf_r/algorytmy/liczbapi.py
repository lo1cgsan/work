from random import uniform
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

def main():
    n = int(input('Podaj liczbę punktów: '))
    p_k = 0
    r = 1

    plt.axvline()
    plt.axhline()
    rect = Rectangle((-1, -1), 2, 2, lw=2, ec="k", fc="none")
    cir = Circle((0, 0), r, lw=2, ec="k", fill=False)
    plt.gca().add_patch(rect)
    plt.gca().add_patch(cir)

    for i in range(n):
        x = uniform(-r, r)
        y = uniform(-r, r)
        print(x, y)
        if x**2 + y**2 < r**2:
            p_k += 1
            plt.plot(x, y, "r.")
        else:
            plt.plot(x, y, "g.")

    print(4 * p_k / n)
    print(math.pi)

    plt.show()

main()