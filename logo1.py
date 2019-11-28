#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  logo1.py
import turtle
import math
import random


def kwadrat(bok, x, y, kolor=(0, 0, 0)):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.pencolor(kolor)
    for i in range(4):
        turtle.forward(bok)
        turtle.left(90)


def kolo(promien, x=0, y=0, kolor=(0, 0, 0)):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.pencolor(kolor)
    turtle.circle(promien)


def losujKolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def kwadraty():
    ile = 5
    bok = 100
    # krok = 40

    for i in range(ile):
        x = bok / 2
        kolor = losujKolor()
        kwadrat(bok, -x, -x, kolor)
        r = math.sqrt(x**2 + x**2)
        # kolo(bok / 2, 0, -bok / 2)
        kolor = losujKolor()
        kolo(r, 0, -r, kolor)
        bok = 2 * r


def gwiazdy():
    ile = 10
    bok = 100
    krok = 20
    kat = 144

    for i in range(ile):
        for j in range(5):
            turtle.forward(bok + krok * i)
            turtle.right(kat)


def rysujKola():
    r = 50
    pozycje = [(0, 0), (-120, 0), (60, 60),
               (-60, 60), (-180, 60)]
    for x, y in pozycje:
        kolor = losujKolor()
        kolo(r, x, y, kolor)


def main(args):
    turtle.setup(800, 600)
    turtle.colormode(255)
    # turtle.pencolor("green")
    turtle.pencolor(0, 255, 0)
    turtle.pensize(5)
    # kwadrat(100, -50, -50)
    # gwiazdy()
    # kwadraty()
    rysujKola()
    turtle.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
