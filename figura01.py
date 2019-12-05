#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle


def proba1():
    turtle.penup()
    turtle.setpos(0, 0)
    turtle.pendown()
    turtle.color("green")
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    for i in range(5):
        turtle.forward(120)
        turtle.right(144)


def proba2():
    ile = 10
    bok = 100
    krok = 20
    kat = 144
    for i in range(ile):
        for j in range(5):
            turtle.forward(bok + (i * krok))
            turtle.right(kat)


def main(args):
    turtle.setup(800, 600)
    turtle.color("red")
    turtle.pensize(3)

    for i in range(4):
        turtle.forward(200)
        turtle.left(90)

    proba2()

    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
