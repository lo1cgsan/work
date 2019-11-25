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

def kwadraty():
    pass

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
    kwadrat(100, -50, -50)
    # gwiazdy()
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
