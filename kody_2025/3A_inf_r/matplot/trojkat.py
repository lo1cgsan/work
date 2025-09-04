from punkt import Punkt
import matplotlib.pyplot as plt


def pobierz_punkty(punkty, nazwy):
    for n in nazwy:
        p = Punkt(n)  # utworzenie obiektu
        print('Punkt:', p)
        p.x = float(input('Podaj x: '))
        p.y = float(input('Podaj y: '))
        punkty.append(p)

def wykresl(punkty):
    lx = []
    ly = []
    for p in punkty[0:3]:
        lx.append(p.x)
        ly.append(p.y)
    lx.append(punkty[0].x)
    ly.append(punkty[0].y)
    plt.plot(lx, ly, 'bo-')
    plt.plot(punkty[-1].x, punkty[-1].y, 'gs')
    plt.show()


def main():
    punkty = []
    pobierz_punkty(punkty, "ABCP")
    wykresl(punkty)

main()
