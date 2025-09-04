from punkt import Punkt
import matplotlib.pyplot as plt


def prosta(x, a=1, b=1):
    y = a * x + b
    return y

def pobierz_punkty(punkty, nazwy):
    for n in nazwy:
        p = Punkt(n)  # utworzenie obiektu
        print('Punkt:', p)
        p.x = float(input('Podaj x: '))
        p.y = float(input('Podaj y: '))
        punkty.append(p)

def wykresl(punkty, a, b):
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

def czy_na_prostej(a, b, punkty):
    for p in punkty:
        if p.y == prosta(p.x, a, b):
            print('Punkt p należy!')
        else:
            print('Punkt p nie należy!')

def main():
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    print(f'Rownanie prostej: y = {a} * x + {b}')
    punkty = []
    pobierz_punkty(punkty, "AB")
    czy_na_prostej(a, b, punkty)
    wykresl(punkty)

main()
