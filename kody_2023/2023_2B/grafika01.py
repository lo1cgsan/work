import turtle

def rysuj_kwadrat(ttl, x, y, bok, kierunek=True):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for i in range(4):
        ttl.forward(bok)
        if kierunek:
            ttl.left(90)
        else:
            ttl.right(90)

def main():
    turtle.title('Figury geometryczne')
    turtle.setup(800, 800, 0, 0)
    # obiekt żółwia
    ttl = turtle.Turtle()

    ttl.color('red')
    rysuj_kwadrat(ttl, 0, 0, 70, True)

    ttl.color('green')
    rysuj_kwadrat(ttl, 70, 0, 70, False)

    turtle.done()

main()

