import turtle
import math

def rysuj_kwadrat(ttl, x, y, bok, kierunek, k_tla, k_wyp):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()

    ttl.color(k_tla)
    ttl.fillcolor(k_wyp)
    ttl.begin_fill()
    for i in range(4):
        ttl.forward(bok)
        ttl.left(90) if kierunek else ttl.right(90)
    ttl.end_fill()

def rysuj_kolo(ttl, x, y, r, kolor='red'):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.color(kolor)
    ttl.circle(r)

def rysuj_wielokat(ttl, x, y, ile_bokow, promien):
    dl_boku = 2 * promien * math.sin(math.pi / ile_bokow)
    kat = 360 / ile_bokow
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for i in range(ile_bokow):
        ttl.forward(dl_boku)
        ttl.left(kat)

def main():
    turtle.title('Figury geometryczne')
    turtle.setup(800, 800, 0, 0)
    ttl = turtle.Turtle()
    rysuj_wielokat(ttl, -100, -100, 3, 60)
    # rysuj_kwadrat(ttl, 0, 0, 70, True, 'red', 'red')
    # rysuj_kwadrat(ttl, 70, 0, 70, False, 'green', 'green')
    r = 60
    rysuj_kolo(ttl, 0, 0, r, 'blue')
    rysuj_kolo(ttl, 2 * r + 10, 0, r, 'black')
    rysuj_kolo(ttl, 4 * r + 20, 0, r, 'red')
    rysuj_kolo(ttl, r + 5, -r, r, 'green')
    rysuj_kolo(ttl, 3 * r + 10, -r, r, 'green')


    turtle.done()


main()
