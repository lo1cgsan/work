import turtle
import math

def rysuj_wielokat(ttl, x, y, ile_bokow, promien):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()

    dl_boku = 2 * promien * math.sin(math.pi / ile_bokow)
    kat = 360 // ile_bokow
    for i in range(ile_bokow):
        ttl.forward(dl_boku)
        ttl.left(kat)


def main():
    turtle.title('Figury geometryczne')
    turtle.setup(800, 800, 0, 0)
    # obiekt żółwia
    ttl = turtle.Turtle()

    ttl.color('red')
    rysuj_wielokat(ttl, 0, 0, 5, 60)

    turtle.done()

main()

