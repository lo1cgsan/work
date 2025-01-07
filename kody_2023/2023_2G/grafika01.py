import turtle as t
import math


def rysuj_kwadrat(ttl, x, y, bok, kierunek):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for i in range(4):
        ttl.forward(bok)
        if kierunek:
            ttl.left(90)
        else:
            ttl.right(90)

def rysuj_kolo(ttl, x, y, r, kolor):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.color(kolor)
    ttl.circle(r)

def rysuj_wielokat(ttl, x, y, ile_bokow, R, kolor):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.color(kolor)
    dl_boku = 2 * R * math.sin(math.pi / ile_bokow)
    kat = 360 / ile_bokow
    for i in range(ile_bokow):
        ttl.forward(dl_boku)
        ttl.left(kat)

def main():
    t.title('Figury geometryczne')
    t.setup(800, 800, 0, 0)
    ttl = t.Turtle()
    rysuj_wielokat(ttl, -100, -100, 3, 70, 'green')
    # rysuj_kwadrat(ttl, 0, 0, 80, False)
    # rysuj_kwadrat(ttl, 80, -80, 80, False)
    # rysuj_kolo(ttl, 0, 0, 60, 'blue')

    t.done()


main()
