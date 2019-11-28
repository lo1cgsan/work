#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  logo1.py
import turtle


def kwadrat(bok, x, y):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)


def kolo(promien, x=0, y=0):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.circle(promien)


def kwadraty():
    ile = 5
    bok = 100
    krok = 40

    for i in range(ile):
        bok = bok + krok
        x = bok / 2
        print(i, bok, x)
        kwadrat(bok, -x, -x)
        kolo(bok / 2, 0, -bok / 2)


def gwiazdy():
    ile = 10
    bok = 100
    krok = 20
    kat = 144

    for i in range(ile):
        for j in range(5):
            turtle.forward(bok + krok * i)
            turtle.right(kat)


def main(args):
    turtle.setup(800, 600)
    turtle.pencolor("green")
    turtle.pensize(5)
    # kwadrat(100, -50, -50)
    # gwiazdy()
    kwadraty()
    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
