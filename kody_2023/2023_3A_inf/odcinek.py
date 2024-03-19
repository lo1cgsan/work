import matplotlib.pyplot as plt
import matplotlib.pylab as plt

from klasa_punkt import pobierz_punkty


def wykres(punkty):
    plt.axhline()
    plt.axvline()
    for p in punkty:
        plt.plot(p.x, p.y, 'r.')
        plt.text(p.x+0.15, p.y-0.15, p)
        plt.vlines(p.x, 0, p.y, ls='--')
        plt.hlines(p.y, 0, p.x, ls='--')
    a, b, c = punkty
    plt.plot((a.x, b.x), (a.y, b.y), 'rs-')
    plt.show()


def main():
    punkty = []
    pobierz_punkty(punkty, 'ABC')
    wykres(punkty)


main()