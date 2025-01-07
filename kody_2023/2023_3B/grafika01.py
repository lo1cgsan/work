import turtle

def rysuj_kwadrat(ttl, x, y, bok, kier=True, k1='black', k2='blue'):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.color(k1)
    ttl.fillcolor(k2)
    ttl.begin_fill()
    for i in range(4):
        ttl.forward(bok)
        if kier:
            ttl.left(90)
        else:
            ttl.right(90)
    ttl.end_fill()


def main():
    turtle.title('Figury geometryczne')
    turtle.setup(800, 800, 0, 0)

    ttl = turtle.Turtle()

    rysuj_kwadrat(ttl, 0, 0, 70, True, 'orange', 'yellow')
    rysuj_kwadrat(ttl, 0, 0, 70, False, 'green', 'orange')

    turtle.done()


main()
