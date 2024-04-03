import matplotlib.pyplot as plt

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


def czy_na_prostej(punkty):
    a, b, c = punkty
    return (b.x - a.x) * (c.y - a.y) == (b.y - a.y) * (c.x -a.x)


def czy_na_odcinku(punkty):
    a, b, c = punkty
    return c.x >= min(a.x, b.x) and c.x <= max(a.x, b.x) and \
           c.y >= min(a.y, b.y) and c.y <= max(a.y, b.y)

def main():
    punkty = []
    pobierz_punkty(punkty, 'ABC')
    wykres(punkty)
    if czy_na_prostej(punkty):
        print("Współliniowe")
        if czy_na_odcinku(punkty):
            print("Przynależy")
        else:
            print("Nie przynależy")
    else:
        print("Niewspółliniowe")


main()
