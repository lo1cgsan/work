import turtle

def rysuj_kolo(ttl, x, y, r):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.circle(r)

def main():
    turtle.title('Figury geometryczne')
    turtle.setup(800, 800, 0, 0)
    # obiekt żółwia
    ttl = turtle.Turtle()

    ttl.color('red')
    rysuj_kolo(ttl, 0, 0, 60)

    turtle.done()

main()

