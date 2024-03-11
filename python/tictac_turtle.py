#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle as t


def kwadrat(bok, x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for i in range(4):
        t.forward(bok)
        t.right(90)


def main(args):
    t.setup(800, 300)
    t.bgcolor("black")
    t.pencolor("white")
    t.pensize(2)
    bok = 90
    x = 0
    y = 100
    for i in range(3):
        for j in range(3):
            print(i, j)
            kwadrat(bok, x + j * bok, y - i * bok)
    # kwadrat(bok, x, y)
    # kwadrat(bok, x + bok, y)
    # kwadrat(bok, x + 2 * bok, y)
    # kwadrat(bok, x, y - bok)
    # kwadrat(bok, x + bok, y - bok)
    # kwadrat(bok, x + 2 * bok, y - bok)
    # kwadrat(bok, x, y - 2 * bok)
    # kwadrat(bok, x + bok, y - 2 * bok)
    # kwadrat(bok, x + 2 * bok, y - 2 * bok)
    t.done()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
